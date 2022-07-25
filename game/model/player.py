"""
Contains Player class and all methods to interact with a player
"""

import game.view.player_interface as i_f
import game.model.hotel as hotel

from abc import ABC
from typing import List, Optional


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
        self.__ui = self.make_interface()
        self.__money = 12000    # standard start of the game
        self.__property_list: List[Optional[hotel.Hotel]] = list()

    def __eq__(self, other):
        return self.__name == other.get_name()

    def make_interface(self) -> i_f.PlayerInterface:
        """
        Set up interface based on the type of the Player
        """
        return i_f.PlayerInterface()

    def get_name(self) -> str:
        return self.__name

    def get_ui(self) -> i_f.PlayerInterface:
        return self.__ui

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

    def get_property_list(self) -> List[Optional[hotel.Hotel]]:
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

    def make_interface(self) -> i_f.PlayerInterface:
        return i_f.HumanInterface()


class AiPlayer(Player):
    """
    AI player instance with correct interface
    """

    def make_interface(self) -> i_f.PlayerInterface:
        return i_f.AiInterface()