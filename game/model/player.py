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
        :param name: unique id of the player
        """
        self.__name = name
        self.__money = 12000    # standard start of the game
        self.__property_list: list[hotel.Hotel or None] = list()

    def __eq__(self, other):
        return self.__name == other.get_name()

    def __hash__(self):
        return hash(self.__name)

    @abstractmethod
    def __repr__(self) -> str:
        """
        :return: internal representation of the object
        """

    @abstractmethod
    def set_interface(self) -> i_f.PlayerInterface:
        """
        Set up interface based on the type of the Player
        """

    def get_name(self) -> str:
        return self.__name

    @abstractmethod
    def get_ui(self) -> i_f.PlayerInterface:
        """
        :return: User Interface
        """

    def get_money(self) -> int:
        return self.__money

    def is_broke(self) -> bool:
        """
        :return: True if the player has no more money left
        """
        return self.__money == 0

    def change_money(self,
                     amount: int
                     ) -> None:
        """
        :param amount: int, negative -> removing money, positive -> adding money
        """
        self.__money += amount

    def get_property_list(self) -> list[hotel.Hotel or None]:
        return self.__property_list

    def add_property(self,
                     h: hotel.Hotel
                     ) -> None:
        """
        :param h: hotel to add as a player property
        """
        self.__property_list.append(h)

    def remove_property(self,
                        h: hotel.Hotel
                        ) -> bool:
        """
        :param h: hotel to remove from player's properties
        :return True if the property was found and successfully removed
                False else
        """
        try:
            self.__property_list.remove(h)
            return True
        except ValueError:
            return False


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
        _repr = (
            f'Player: {self.get_name()}\n'
            f'\tType: Human\n'
            f'\tMoney: {self.get_money()}\n'
            f'\tProperty List: {self.get_property_list()}'
        )
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
        _repr = (
            f'Player: {self.get_name()}\n'
            f'\tType: AI\n'
            f'\tMoney: {self.get_money()}\n'
            f'\tProperty List: {self.get_property_list()}'
        )
        return _repr
