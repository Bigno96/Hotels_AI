import unittest
import unittest.mock as mock

import game.model.player as player
import game.view.player_interface as i_f


class PlayerTest(unittest.TestCase):

    def test_init(self):
        human_pl = player.HumanPlayer(name='human')
        ai_pl = player.AiPlayer(name='AI')

        human_copy = player.HumanPlayer(name='human')

        self.assertEqual(human_pl.get_name(), 'human')
        self.assertEqual(ai_pl.get_name(), 'AI')

        self.assertEqual(human_pl, human_copy)
        self.assertNotEqual(ai_pl, human_pl)

        self.assertIsInstance(human_pl.get_ui(), i_f.HumanInterface)
        self.assertIsInstance(ai_pl.get_ui(), i_f.AiInterface)

    @staticmethod
    def test_print():
        human_pl = player.HumanPlayer(name='human')
        ai_pl = player.AiPlayer(name='AI')
        print(human_pl)
        print(ai_pl)

    def test_hash_eq(self):
        human_pl = player.HumanPlayer(name='human')
        ai_pl = player.AiPlayer(name='AI')
        human_copy = player.HumanPlayer(name='human')
        ai_copy = player.HumanPlayer(name='AI')

        self.assertEqual(human_pl, human_copy)
        self.assertEqual(ai_pl, ai_copy)
        self.assertNotEqual(human_pl, ai_pl)

        self.assertEqual(hash(human_pl), hash(human_copy))
        self.assertEqual(hash(ai_pl), hash(ai_copy))
        self.assertNotEqual(hash(human_pl), hash(ai_pl))

    def test_money(self):
        pl = player.HumanPlayer(name='test_player')

        self.assertEqual(pl.get_money(), 12000)  # init value

        pl.change_money(amount=1000)
        self.assertEqual(pl.get_money(), 13000)  # 12000 + 1000

        pl.change_money(amount=-3000)
        self.assertEqual(pl.get_money(), 10000)  # 13000 - 3000

        self.assertFalse(pl.is_broke())

        pl.change_money(amount=-10000)
        self.assertTrue(pl.is_broke())

    def test_property(self):
        pl = player.HumanPlayer(name='test_player')

        self.assertFalse(pl.get_property_list())

        hotel = mock.Mock()
        hotel.get_name.return_value = 'test_hotel'

        pl.remove_property(h=hotel)
        self.assertFalse(pl.get_property_list())

        pl.add_property(h=hotel)
        self.assertIn(hotel, pl.get_property_list().values())

        pl.remove_property(h=hotel)
        self.assertFalse(pl.get_property_list())


if __name__ == '__main__':
    unittest.main()
