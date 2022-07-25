"""
Testing module for Cell class
"""

import unittest
import unittest.mock as mock

import game.model.cell as cell
import utils.config as cfg

from easydict import EasyDict
from random import randint

CELL_JSON_PATH = "D:/Hotels_AI/configs/cell.json"


class CellTest(unittest.TestCase):

    def test_init(self):
        cell_dict = cfg.get_config_from_json(CELL_JSON_PATH)

        # test initialization of all cells
        for i in range(-1, 31): # last cell id is 30

            c = set_cell(i)
            c_json = cell_dict[str(i)]

            self.assertEqual(c.get_id(), i)
            self.assertEqual(c.get_type(), c_json["type"])
            self.assertEqual(c.get_hotels_near(), c_json["hotels_near"])
            self.assertIsInstance(c.get_hotels_near(), list)
            self.assertIsNone(c.get_entrance())
            self.assertFalse(c.is_occupied())

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
    config = EasyDict()
    config.cell_dict = cfg.get_config_from_json(CELL_JSON_PATH)

    return cell.Cell(ID=idx, config=config)


if __name__ == '__main__':
    unittest.main()
