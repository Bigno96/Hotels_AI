"""
Contains Board class and all methods to control the board
"""

import game.model.cell as cell
import game.model.player as player

from typing import List
from easydict import EasyDict


class Board:
    """
    Board class
    """

    def __init__(self,
                 config: EasyDict,
                 player_list: List[player.Player]):
        """
        :param config: global config dictionary
        :param player_list: list of players in the game
        """
        self.__cell_list : List[cell.Cell] = [cell.Cell(ID=i, config=config)
                                              for i in range(-1, 31)]   # last cell id is 30
        start_cell = [c for c in self.__cell_list
                      if c.get_id() == -1][0]    # first cell
        self.__position_trace : EasyDict[player.Player, cell.Cell] = EasyDict({
            p:start_cell
            for p in player_list
        })

    def find_cell(self,
                  cell_id: int
                  ) -> cell.Cell:
        """
        :param cell_id: id of the cell
        :return: Cell instance with given id
        :raise IndexError if the id is out of bounds
        """
        if cell_id < -1 or cell_id > 30:    # id out of bounds
            raise IndexError
        # return the cell
        return [c for c in self.__cell_list
                if c.get_id() == cell_id][0]