import unittest
import unittest.mock as mock

import game.model.player as player
import game.view.player_interface as i_f


class PlayerTest(unittest.TestCase):

    def test_init(self):
        human_p = player.HumanPlayer(name='human')
        ai_p = player.AiPlayer(name='AI')

        human_copy = player.HumanPlayer(name='human')

        self.assertEqual(human_p.get_name(), 'human')
        self.assertEqual(ai_p.get_name(), 'AI')

        self.assertEqual(human_p, human_copy)
        self.assertNotEqual(ai_p, human_p)

        self.assertIsInstance(human_p.get_ui(), i_f.HumanInterface)
        self.assertIsInstance(ai_p.get_ui(), i_f.AiInterface)

    @staticmethod
    def test_print():
        human_p = player.HumanPlayer(name='human')
        ai_p = player.AiPlayer(name='AI')
        print(human_p)
        print(ai_p)

    def test_hash_eq(self):
        human_p = player.HumanPlayer(name='human')
        ai_p = player.AiPlayer(name='AI')
        human_copy = player.HumanPlayer(name='human')
        ai_copy = player.HumanPlayer(name='AI')

        self.assertEqual(human_p, human_copy)
        self.assertEqual(ai_p, ai_copy)
        self.assertNotEqual(human_p, ai_p)

        self.assertEqual(hash(human_p), hash(human_copy))
        self.assertEqual(hash(ai_p), hash(ai_copy))
        self.assertNotEqual(hash(human_p), hash(ai_p))

    def test_money(self):
        p = player.HumanPlayer(name='test')

        self.assertEqual(p.get_money(), 12000)  # init value

        p.change_money(amount=1000)
        self.assertEqual(p.get_money(), 13000)  # 12000 + 1000

        p.change_money(amount=-3000)
        self.assertEqual(p.get_money(), 10000)  # 13000 - 3000

        self.assertFalse(p.is_broke())

        p.change_money(amount=-10000)
        self.assertTrue(p.is_broke())

    def test_property(self):
        p = player.HumanPlayer(name='test')

        self.assertFalse(p.get_property_list())

        h = mock.Mock()

        self.assertFalse(p.remove_property(h=h))

        p.add_property(h=h)
        self.assertIn(h, p.get_property_list())

        self.assertTrue(p.remove_property(h=h))
        self.assertFalse(p.get_property_list())

        self.assertFalse(p.remove_property(h=h))


if __name__ == '__main__':
    unittest.main()
