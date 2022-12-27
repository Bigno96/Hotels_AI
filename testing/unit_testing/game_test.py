import unittest
import random

from easydict import EasyDict

from game.model.game import Game
from utils.config import process_config

class MyTestCase(unittest.TestCase):

    @staticmethod
    def test_print():
        config = process_config(EasyDict())
        game = Game(config=config)

        # list of player and hotel names
        pl_names = game.get_player_list().keys()
        hotel_names = game.get_hotel_list().keys()

        # obtain 3 random hotels
        htl1, htl2, htl3 = random.sample(list(hotel_names), k=3)
        htl1 = game.get_hotel(name=htl1)
        htl2 = game.get_hotel(name=htl2)
        htl3 = game.get_hotel(name=htl3)
        # obtain 2 random players
        pl1, pl2 = random.sample(list(pl_names), k=2)
        pl1 = game.get_player(name=pl1)
        pl2 = game.get_player(name=pl2)

        # assign properties
        pl1.add_property(h=htl1)
        pl1.change_money(amount=-htl1.get_land_cost())
        pl1.add_property(h=htl2)
        pl1.change_money(amount=-htl2.get_land_cost())
        pl2.add_property(h=htl3)
        pl2.change_money(amount=-htl3.get_land_cost())

        # move players
        game.get_board().move_player(p=pl1, delta=random.randint(1, 6))
        game.get_board().move_player(p=pl2, delta=random.randint(1, 6))

        print(game)

    def test_player(self):
        config = process_config(EasyDict())
        game = Game(config=config)

        # remove based on player name
        player_name_list = game.get_player_list().keys()
        pl_name = random.choice(list(player_name_list))
        game.remove_player(name=pl_name)

        self.assertNotIn(pl_name,
                         game.get_player_list().keys())

        # remove based on player instance
        player_name_list = game.get_player_list().keys()
        pl_name = random.choice(list(player_name_list))
        pl = game.get_player(name=pl_name)
        game.remove_player(p=pl)

        self.assertNotIn(pl_name,
                         game.get_player_list().keys())

        # test assertion error
        self.assertRaises(IndexError,
                          lambda: game.get_player(name=pl_name))
        self.assertRaises(AssertionError,
                          lambda: game.remove_player())

    def test_hotel(self):
        config = process_config(EasyDict())
        game = Game(config=config)

        hotel_name_list = game.get_hotel_list().keys()
        hotel_name = random.choice(list(hotel_name_list))

        hotel = game.get_hotel(name=hotel_name)

        self.assertEqual(hotel.get_name(), hotel_name)


if __name__ == '__main__':
    unittest.main()
