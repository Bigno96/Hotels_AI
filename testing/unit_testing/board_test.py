"""
Testing module for Board class
"""

import unittest

import utils.config as cfg
import game.model.player as pl
import game.model.board as brd

from easydict import EasyDict
from random import sample, randint

from unit_testing import CELL_YAML_PATH

PLAYER_COUNT = 4
REPETITION = 1000


class BoardTest(unittest.TestCase):

    def test_board_cell(self):
        config = EasyDict()
        config.cell_dict = cfg.get_config_from_yaml(CELL_YAML_PATH)
        player_list = create_player_list(n_players=PLAYER_COUNT,
                                         player_type='human')   # doesn't matter type

        board = brd.Board(config=config,
                          player_list=player_list)

        # test find cells
        for i in range(-1, 31):     # max id is 30
            c = board.find_cell(i)
            self.assertEqual(c.get_id(), i)

    def test_move_players(self):
        for _ in range(REPETITION):
            config = EasyDict()
            config.cell_dict = cfg.get_config_from_yaml(CELL_YAML_PATH)
            player_list = create_player_list(n_players=PLAYER_COUNT,
                                             player_type='human')   # doesn't matter type

            board = brd.Board(config=config,
                              player_list=player_list)

            '''all players in starting cell'''
            for p in player_list:
                self.assertEqual(-1,
                                 board.find_player_pos(p).get_id())

            '''move player'''
            p, p_start = sample(player_list, k=2)
            dest = board.find_cell(cell_id=randint(0, 30))
            delta = randint(0, 6)

            # move using dest
            board.move_player(p=p, dest=dest, delta=delta)
            self.assertEqual(board.find_player_pos(p=p).get_id(),
                             dest.get_id())

            # move using delta
            board.move_player(p=p, dest=None, delta=delta)
            delta_id = (dest.get_id() + delta) % 31
            self.assertEqual(board.find_player_pos(p=p).get_id(),
                             delta_id)

            # others did not move
            for p1 in player_list:
                if p1 != p:
                    self.assertEqual(-1,
                                     board.find_player_pos(p1).get_id())

            # test delta when being in the starting cell
            board.move_player(p=p_start, dest=None, delta=delta)
            self.assertEqual(board.find_player_pos(p=p_start).get_id(),
                             (delta-1) % 31)   # start cell

            '''remove a player'''
            board.remove_player(p=p)

            self.assertRaises(IndexError,
                              lambda: board.find_player_pos(p=p))
            self.assertRaises(IndexError,
                              lambda: board.remove_player(p=p))
            self.assertRaises(IndexError,
                              lambda: board.move_player(p=p, dest=None, delta=3))

            '''not existing cells'''
            self.assertRaises(IndexError,
                              lambda: board.find_cell(cell_id=31))
            self.assertRaises(IndexError,
                              lambda: board.find_cell(cell_id=-3))


def create_player_list(n_players: int,
                       player_type: str,
                       ) -> list[pl.Player]:
    """
    Instantiate a list of players
    :param n_players: number of players
    :param player_type: 'human' or 'AI'
    :return: list of players
    """
    if player_type.lower() == 'human':
        player_list = [pl.HumanPlayer(name=str(i))
                       for i in range(n_players)]
    else:
        player_list = [pl.AiPlayer(name=str(i))
                       for i in range(n_players)]

    return player_list


if __name__ == '__main__':
    unittest.main()
