"""
Contains Player class and all methods to interact with a player
"""

import game.view.player_interface as i_f
import game.model.hotel as hotel

from abc import ABC, abstractmethod


class Player(ABC):
    """
    Super class of Player instance
    Key: name
    """

    def __init__(self,
                 name: str):
        """
        :param: name: unique id of the player
        """
        self.__name: str = name
        self.__money: int = 12000    # standard start of the game
        self.__property_list: dict[str: hotel.Hotel] = dict()

    def __eq__(self, other):
        return self.__name == other.get_name()

    def __hash__(self):
        return hash(self.__name)

    def __repr__(self) -> str:
        property_list = [f'({prop.get_name()}, {prop.get_star_level()}*)'
                         for prop in list(self.get_property_list().values())]
        _repr = (
            f'Player: {self.get_name()}\n'
            f'\tMoney: {self.get_money()}\n'
            f'\tProperty List: {property_list}\n'
        )

        return _repr

    @abstractmethod
    def set_interface(self) -> i_f.PlayerInterface:
        """
        Set up interface based on the type of the Player
        """

    def get_name(self) -> str:
        """
        :return: name of the player
        """
        return self.__name

    @abstractmethod
    def get_ui(self) -> i_f.PlayerInterface:
        """
        :return: User Interface
        """

    def get_money(self) -> int:
        """
        :return: money owned by the player
        """
        return self.__money

    def is_broke(self) -> bool:
        """
        :return: True if the player has no more money left
        """
        return self.__money <= 0

    def change_money(self,
                     amount: int
                     ) -> None:
        """
        :param: amount: int, negative -> removing money, positive -> adding money
        """
        self.__money += amount

    def get_property_list(self) -> dict[str:hotel.Hotel]:
        """
        :return: property list of the player
        """
        return self.__property_list

    def add_property(self,
                     h: hotel.Hotel
                     ) -> None:
        """
        :param: h: hotel to add as a player property
        """
        self.__property_list[h.get_name()] = h

    def remove_property(self,
                        h: hotel.Hotel = None,
                        name: str = None
                        ) -> None:
        """
        In case both parameters are specified, hotel.get_name overrides name
        :param h: hotel to remove from player's properties
        :param name: name of the hotel to remove from player's properties
        :raise AssertionError if neither hotel nor name are specified
        """
        assert h or name, f'No property specified'
        if h:
            name = h.get_name()
        if name in self.__property_list.keys():
            del self.__property_list[name]


class HumanPlayer(Player):
    """
    Human player instance with correct interface
    """

    def __init__(self,
                 name: str):
        super(HumanPlayer, self).__init__(name=name)
        self.__ui = self.set_interface()

    def set_interface(self) -> i_f.PlayerInterface:
        return i_f.HumanInterface()

    def get_ui(self) -> i_f.PlayerInterface:
        return self.__ui

    def __repr__(self) -> str:
        _repr = super(HumanPlayer, self).__repr__()
        _repr += f'\tType: Human\n'
        return _repr


class AiPlayer(Player):
    """
    AI player instance with correct interface
    """

    def __init__(self,
                 name: str):
        super(AiPlayer, self).__init__(name=name)
        self.__ui = self.set_interface()

    def set_interface(self) -> i_f.PlayerInterface:
        return i_f.AiInterface()

    def get_ui(self) -> i_f.PlayerInterface:
        return self.__ui

    def __repr__(self) -> str:
        _repr = super(AiPlayer, self).__repr__()
        _repr += f'\tType: AI\n'
        return _repr
