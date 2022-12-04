"""
Contains Cell class and all methods to manipulate a cell instance
"""

import game.model.hotel as hotel

from easydict import EasyDict


class Cell:
    """
    Cell class
    Key: ID
    """

    def __init__(self,
                 ID: int,
                 config: EasyDict):
        """
        Build Cell reading configuration
        :param ID: ID of the cell
        :param config: global config dictionary
        """
        self.__id: int = ID
        self.__config = config

        cell = config.cell_dict[str(ID)]
        self.__type: int = cell.type
        self.__hotels_near: list[str] = cell.hotels_near

        self.__hotel_entrance: hotel.Hotel or None = None
        self.__occupied: bool = False

    def __eq__(self, other):
        return self.__id == other.get_id()

    def __hash__(self):
        return hash(self.__id)

    def __repr__(self):
        _repr = (
            f'Cell: {self.__id}\n'
            f'\tType: {self.__config.cell_type_dict[str(self.__type)]}\n'
            f'\tHotels Near: {self.__hotels_near}\n'
            f'\tHotel Entrance: {self.__hotel_entrance}\n'
            f'\tOccupied: {self.__occupied}'
        )
        return _repr

    def get_id(self) -> int:
        """
        :return: ID (key value) of the cell
        """
        return self.__id

    def get_type(self) -> int:
        """
        :return: type of the cell, as int
        """
        return self.__type

    def get_hotels_near(self) -> list[str]:
        """
        :return: list of Hotel names that are adjacent to the cell
        """
        return self.__hotels_near

    def get_entrance(self) -> hotel.Hotel or None:
        """
        :return: None if no entrance, else the Hotel object which has entrance on the cell
        """
        return self.__hotel_entrance

    def add_entrance(self,
                     h: hotel.Hotel
                     ) -> None:
        """
        Add entrance to the cell
        :param h: Hotel object
        """
        self.__hotel_entrance = h

    def is_occupied(self) -> bool:
        """
        :return: True if cell is occupied by a player car, False else
        """
        return self.__occupied

    def occupy(self) -> None:
        """
        Set occupied = True when a player occupies the cell
        """
        self.__occupied = True

    def free(self) -> None:
        """
        Set occupied = False when a player leaves the cell
        """
        self.__occupied = False


