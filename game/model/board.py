"""
Contains Board class and all methods to control the board
"""

import game.model.cell as cell
import game.model.player as player

from easydict import EasyDict
from typing import Iterable


class Board:
    """
    Board class
    """

    def __init__(self,
                 config: EasyDict,
                 player_list: Iterable[player.Player]):
        """
        :param config: global config dictionary
        :param player_list: list of players in the game
        """
        self.__cell_list: dict[int: cell.Cell] = {
            i: cell.Cell(cell_id=i, config=config)
            for i in range(-1, 31)}   # last cell id is 30
        self.__position_trace: dict[player.Player: cell.Cell] = {
            p: self.__cell_list[-1]
            for p in player_list
        }

    def __repr__(self):
        _repr = 'Board: \n'
        for pl, pos in self.__position_trace.items():
            _repr += f'\t{pl.get_name()} | Cell: {pos.get_id()}\n'

        return _repr

    def find_cell(self,
                  cell_id: int
                  ) -> cell.Cell:
        """
        Find a cell in the board
        :param cell_id: id of the cell
        :return: Cell instance with given id
        :raise IndexError if the id is out of bounds
        """
        if cell_id in self.__cell_list.keys():
            return self.__cell_list[cell_id]
        raise IndexError(f'Could not find Cell {cell_id} in the board')

    def find_player_pos(self,
                        p: player.Player
                        ) -> cell.Cell:
        """
        Find the cell the player is standing in
        :param p: Player to find
        :return: Cell instance
        :raise IndexError if the player is not in the board
        """
        if p in self.__position_trace.keys():
            return self.__position_trace[p]
        raise IndexError(f'Could not find Player {p.get_name()} in the board')

    def remove_player(self,
                      p: player.Player
                      ) -> None:
        """
        Remove the player from the board
        :param p: Player to be removed
        :raise IndexError if the player is not in the board
        """
        if p not in self.__position_trace.keys():
            raise IndexError(f'Could not find Player {p.get_name()} in the board')
        del self.__position_trace[p]

    def move_player(self,
                    p: player.Player,
                    dest: cell.Cell = None,
                    delta: int = 0
                    ) -> None:
        """
        Move the player around the board
        If dest is specified, move to dest
        Else use delta to move
        Default: stand still
        :param p: Player to move
        :param dest: Cell to move to
        :param delta: difference in cell id of player position
                      i.e., dice roll value or number of cells to move
        :raise IndexError if the player is not in the board
        """
        if p not in self.__position_trace.keys():
            raise IndexError(f'Could not find Player {p.get_name()} in the board')
        c = self.__position_trace[p]

        # move to dest
        if dest:
            self.__position_trace[p] = dest
            return

        # else, use delta
        # first get new pos
        new_cell_idx = (c.get_id() + delta) % 31    # modulo takes care of the sign of delta
        new_cell = self.__cell_list[new_cell_idx]
        # second, move to cell
        self.__position_trace[p] = new_cell
