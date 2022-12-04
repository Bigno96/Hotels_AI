"""
Testing module for Cell class
"""

import unittest
import random

import game.model.hotel as hotel
import utils.config as cfg

from unit_testing import HOTEL_JSON_PATH, HOTEL_NAMES, HOTEL_UPGRADE_TYPE_JSON_PATH


class HotelTest(unittest.TestCase):

    def test_init(self):
        hotel_dict = cfg.get_config_from_json(HOTEL_JSON_PATH)

        for name in HOTEL_NAMES:

            h = set_hotel(name=name)
            h_json = hotel_dict[name]

            h_copy = set_hotel(name=name)
            self.assertEqual(h, h_copy)

            # test name
            self.assertEqual(h.get_name(), name)

            # test costs
            self.assertEqual(h.get_land_cost(), h_json.land_cost)
            self.assertEqual(h.get_expropriation_price(), h_json.expropriation_price)
            self.assertEqual(h.get_entrance_cost(), h_json.entrance_cost)

    @staticmethod
    def test_print():
        name = random.choice(HOTEL_NAMES)
        h = set_hotel(name=name)
        print(h)

    def test_hash_eq(self):
        name1, name2 = random.sample(HOTEL_NAMES, k=2)
        h1 = set_hotel(name=name1)
        h1_copy = set_hotel(name=name1)
        h2 = set_hotel(name=name2)

        self.assertEqual(h1, h1_copy)
        self.assertNotEqual(h1, h2)

        self.assertEqual(hash(h1), hash(h1_copy))
        self.assertNotEqual(hash(h1), hash(h2))

    def test_owner(self):
        name = random.choice(HOTEL_NAMES)
        h = set_hotel(name=name)

        self.assertIsNone(h.get_owner())

        # mocking Player instance
        player = 'test'

        h.set_owner(player_name=player)
        self.assertEqual(h.get_owner(), 'test')

        h.free_property()
        self.assertIsNone(h.get_owner())

    def test_upgrades(self):
        hotel_dict = cfg.get_config_from_json(HOTEL_JSON_PATH)
        hotel_upgrade_type_dict = cfg.get_config_from_json(HOTEL_UPGRADE_TYPE_JSON_PATH)

        for _ in range(100):
            up_type = random.randint(0, 5)
            name = random.choice(HOTEL_NAMES)
            h = set_hotel(name=name)
            h_json = hotel_dict[name]
            star_level = h_json.star_upgrade[up_type]

            # find upgrade name and cost based on the up_type (integer)
            up_name = [key
                       for key, value
                       in hotel_upgrade_type_dict.items()
                       if value == up_type][0]
            up_cost = h_json.costs[up_name]

            # no previous upgrade
            self.assertEqual(h.get_star_level(), 0)

            costs_table = h.get_upgrade_costs()
            # upgrade not available
            if up_cost == 'None':
                self.assertNotIn(up_name, costs_table.keys())
            # upgrade available
            else:
                self.assertIn(up_name, costs_table.keys())
                self.assertEqual(int(up_cost), costs_table[up_name])

            # do the upgrade
            h.upgrade(up_type)
            self.assertEqual(h.get_star_level(), star_level)
            self.assertEqual(h.get_last_upgrade(), up_type)

            # check that no 'none' upgrade nor upgrade with lower indexes than up_type are present
            costs_table = h.get_upgrade_costs()
            for key in costs_table.keys():
                # if last upgrade == 3, only upgrades of idx 4 and 5 are shown
                self.assertLess(up_type, hotel_upgrade_type_dict[key])
                self.assertIsNotNone(h_json.costs[key])

    def test_payments(self):
        hotel_dict = cfg.get_config_from_json(HOTEL_JSON_PATH)

        for _ in range(1000):
            up_type = random.randint(0, 5)
            name = random.choice(HOTEL_NAMES)
            h = set_hotel(name=name)
            h_json = hotel_dict[name]

            h.upgrade(up_type)
            nights = random.randint(1, 6)
            star_level = h.get_star_level()

            self.assertEqual(h.get_payments()[star_level-1][nights-1],
                             h_json.payments[star_level-1][nights-1])


def set_hotel(name: str
              ) -> hotel.Hotel:
    """
    Instantiate a new hotel with given name
    :param name: id of the cell to create
    :return Hotel with given name
    """
    config = cfg.process_config(None)

    return hotel.Hotel(name=name, config=config)


if __name__ == '__main__':
    unittest.main()
