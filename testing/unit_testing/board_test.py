"""
Testing module for Board class
"""

import unittest

import utils.config as cfg
import game.model.player as pl
import game.model.board as brd

from typing import List
from easydict import EasyDict
from random import randint

CELL_JSON_PATH = "D:/Hotels_AI/configs/cell.json"
PLAYER_COUNT = 4
REPETITION = 1000


class BoardTest(unittest.TestCase):

    def test_board_cell(self):
        config = EasyDict()
        config.cell_dict = cfg.get_config_from_json(CELL_JSON_PATH)
        player_list = create_player_list(n_players=PLAYER_COUNT)

        board = brd.Board(config=config,
                          player_list=player_list)

        # test find cells
        for i in range(-1, 31): # max id is 30
            c = board.find_cell(i)
            self.assertEqual(c.get_id(), i)

    def test_move_players(self):
        for _ in range(REPETITION):
            config = EasyDict()
            config.cell_dict = cfg.get_config_from_json(CELL_JSON_PATH)
            player_list = create_player_list(n_players=PLAYER_COUNT)

            board = brd.Board(config=config,
                              player_list=player_list)

            '''all players in starting cell'''
            for p in player_list:
                self.assertEqual(-1,
                                 board.find_player_pos(p).get_id())

            '''move agent'''
            p = player_list[randint(0, PLAYER_COUNT-1)] # both extremes included
            dest = board.find_cell(cell_id=randint(0, 30))
            delta = randint(0, 6)

            # move using dest
            board.move_player(p=p,
                              dest=dest,
                              delta=delta)
            self.assertEqual(board.find_player_pos(p=p).get_id(),
                             dest.get_id())

            # move using delta
            board.move_player(p=p,
                              dest=None,
                              delta=delta)
            delta_id = (dest.get_id() + delta) % 31
            self.assertEqual(board.find_player_pos(p=p).get_id(),
                             delta_id)

            # others did not move
            for p1 in player_list:
                if p1 != p:
                    self.assertEqual(-1,
                                     board.find_player_pos(p1).get_id())

            '''remove a player'''
            board.remove_player(p=p)

            self.assertRaises(IndexError,
                              lambda: board.find_player_pos(p=p))
            self.assertRaises(IndexError,
                              lambda: board.remove_player(p=p))
            self.assertRaises(IndexError,
                              lambda: board.move_player(p=p,
                                                        dest=None,
                                                        delta=3))
            self.assertRaises(IndexError,
                              lambda: board.find_cell(cell_id=31))
            self.assertRaises(IndexError,
                              lambda: board.find_cell(cell_id=-3))


def create_player_list(n_players: int
                       ) -> List[pl.Player]:
    """
    Instantiate a list of players
    :param n_players: number of players
    :return: list of players
    """
    player_list = []
    for i in range(n_players):
        player_list.append(pl.Player(name=str(i)))

    return player_list


if __name__ == '__main__':
    unittest.main()
