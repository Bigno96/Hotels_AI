"""
Testing module for Cell class
"""
import random
import unittest
import unittest.mock as mock

import game.model.cell as cell
import utils.config as cfg

from random import randint
from easydict import EasyDict
from unit_testing import CELL_YAML_PATH


class CellTest(unittest.TestCase):

    def test_init(self):
        cell_dict = cfg.get_config_from_yaml(CELL_YAML_PATH)

        # test initialization of all cells
        for i in range(-1, 31): # last cell id is 30

            c = set_cell(i)
            c_json = cell_dict[str(i)]

            self.assertEqual(c.get_id(), i)
            self.assertEqual(c.get_type(), c_json.type)
            self.assertEqual(c.get_hotels_near(), c_json.hotels_near)
            self.assertIsInstance(c.get_hotels_near(), list)
            self.assertIsNone(c.get_entrance())
            self.assertFalse(c.is_occupied())

    @staticmethod
    def test_print():
        i = randint(-1, 30)
        c = set_cell(i)
        print(c)

    def test_hash_eq(self):
        # test eq
        i, j = random.sample(range(-1, 31), k=2)
        c_i = set_cell(i)
        c_j = set_cell(j)
        self.assertEqual(c_i, c_i)
        self.assertNotEqual(c_i, c_j)

        # test hash
        self.assertEqual(hash(c_i), hash(c_i))
        self.assertNotEqual(hash(c_i), hash(c_j))

    def test_entrance(self):
        i = randint(-1, 30)
        c = set_cell(idx=i)

        self.assertIsNone(c.get_entrance())

        # mocking hotel instance
        hotel = mock.Mock()
        hotel.get_name.return_value = 'test'

        c.add_entrance(hotel)
        self.assertEqual(c.get_entrance().get_name(), 'test')

    def test_occupancy(self):
        i = randint(-1, 30)
        c = set_cell(idx=i)

        self.assertFalse(c.is_occupied())
        c.occupy()
        self.assertTrue(c.is_occupied())
        c.free()
        self.assertFalse(c.is_occupied())


def set_cell(idx: int
             ) -> cell.Cell:
    """
    Instantiate a new cell with given id
    :param idx: id of the cell to create
    :return Cell with given ID
    """
    config = cfg.process_config(EasyDict())
    return cell.Cell(cell_id=idx, config=config)


if __name__ == '__main__':
    unittest.main()
