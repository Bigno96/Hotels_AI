"""
Contains Hotel class and all methods to manipulate a hotel instance
"""

from prettytable import PrettyTable
from easydict import EasyDict


class Hotel:
    """
    Hotel class
    Key: name
    """

    def __init__(self,
                 name: str,
                 config: EasyDict):
        """
        Build Hotel reading configuration
        :param name: name of the hotel, unique
        :param config: global config dictionary
        """
        self.__name: str = name
        self.__hotel_config: EasyDict = config.hotel_dict[name]
        self.__hotel_upgrade_type_dict: dict[str: int] = config.hotel_upgrade_type_dict
        self.__hotel_upgrade_type_dict_reverse: dict[int: str] = {  # reverse dictionary for easier access on repr
            value: key
            for key, value in self.__hotel_upgrade_type_dict.items()
        }
        self.__owner: str or None = None
        self.__star_level: int = 0
        self.__last_upgrade_idx: int = -1      # keep track of last upgrade

    def __eq__(self, other):
        return self.__name == other.get_name()

    def __hash__(self):
        return hash(self.__name)

    def __repr__(self):
        hotel_cfg = self.__hotel_config

        # get and format last upgrade performed as a string
        last_upgrade = self.__hotel_upgrade_type_dict_reverse[self.__last_upgrade_idx]

        # table for payments
        table = PrettyTable()
        table.field_names = ['1 night', '2 night', '3 night', '4 night', '5 night', '6 night']
        for row in hotel_cfg.payments:
            table.add_row(row)
        table.border = False
        table.left_padding_width = 8

        _repr = (
            f'{self.__name}\n'
            f'\tOwner: {self.__owner}\n'
            f'\t{self.__star_level} star\n'
            f'\tLast upgrade: {last_upgrade}\n'
            f'\tLand cost: {hotel_cfg.land_cost}\n'
            f'\tExpropriation price: {hotel_cfg.expropriation_price}\n'
            f'\tEntrance cost: {hotel_cfg.entrance_cost}\n'
            f'\tCosts:\n'
            f'\t\tmain_building: {hotel_cfg.costs.main_building}\n'
            f'\t\tI_dependance: {hotel_cfg.costs.I_dependance}\n'
            f'\t\tII_dependance: {hotel_cfg.costs.II_dependance}\n'
            f'\t\tIII_dependance: {hotel_cfg.costs.III_dependance}\n'
            f'\t\tIV_dependance: {hotel_cfg.costs.IV_dependance}\n'
            f'\t\tfacilities: {hotel_cfg.costs.facilities}\n'
            f'\tpayments:\n'
            f'{table}\n'
        )
        return _repr

    def get_name(self) -> str:
        """
        :return: name of the Hotel
        """
        return self.__name

    def get_owner(self) -> str or None:
        """
        :return: return Player object who owns the property, None if no player
        """
        return self.__owner

    def set_owner(self,
                  player_name: str
                  ) -> None:
        """
        :param: player_name: name of the player who is currently owning the hotel
        """
        self.__owner = player_name

    def free_property(self) -> None:
        """
        Remove the owner of the property
        """
        self.__owner = None

    def get_star_level(self) -> int:
        """
        :return: current star level of the property
        """
        return self.__star_level

    def get_last_upgrade(self) -> int:
        """
        Return idx for last upgrade of the Hotel
        :return: idx for hotel_upgrade_type_dict
        """
        return self.__last_upgrade_idx

    def upgrade(self,
                upgrade_type: int
                ) -> None:
        """
        Set the star level of the hotel accordingly to the upgrade done
        :param upgrade_type: corresponding to the upgrade type selected
        """
        self.__last_upgrade_idx = upgrade_type
        self.__star_level = self.__hotel_config.star_upgrade[upgrade_type]

    def get_land_cost(self) -> int:
        """
        :return: cost of buying the hotel land
        """
        return self.__hotel_config.land_cost

    def get_expropriation_price(self) -> int:
        """
        :return: expropriation price for the hotel terrain
        """
        return self.__hotel_config.expropriation_price

    def get_entrance_cost(self) -> int:
        """
        :return: cost of buying an entrance for the hotel
        """
        return self.__hotel_config.entrance_cost

    def get_upgrade_costs(self) -> EasyDict:
        """
        Get the upgrade costs of the available building options for the hotel, starting FROM the last built option
        :return: dictionary of costs
        """
        return EasyDict(
            {
                key: value
                for key, value
                in self.__hotel_config.costs.items()  # loop over costs dictionary
                # anything in upgrade_type_dict with value > last_upgrade_idx can be seen
                # e.g., if last_upgrade idx = 3 --> "IV_dependance" (4) and "facilities" (5) can be seen
                if value != 'None' and  # filter upgrades unavailable
                   int(self.__hotel_upgrade_type_dict[key]) > self.__last_upgrade_idx
            }
        )

    def get_payments(self) -> list[list[int]]:
        """
        Return the payment matrix
        Row = number of stars, column = number of nights
        :return: matrix representing payments
        """
        return self.__hotel_config.payments
