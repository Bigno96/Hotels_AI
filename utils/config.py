import json
import os

from easydict import EasyDict

PROJECT_ROOT = 'D:/Hotels_AI'
APPEND_PROJECT_ROOT = True

CELL_JSON_PATH = 'configs/cell.json'
CELL_TYPE_JSON_PATH = 'configs/cell_type.json'
HOTEL_JSON_PATH = 'configs/hotel.json'
HOTEL_UPGRADE_TYPE_JSON_PATH = 'configs/hotel_upgrade_type.json'


def get_config_from_json(json_file: str
                         ) -> EasyDict:
    """
    Get the config from a json file
    :param json_file: the path of the config file
    :return: config(namespace)
    """

    # parse the configurations from the config json file provided
    with open(json_file, 'r') as config_file:
        try:
            config_dict = json.load(config_file)
            # EasyDict allows accessing dict values as attributes (works recursively).
            config = EasyDict(config_dict)
            return config
        except ValueError:
            print('INVALID JSON file format.. Please provide a good json file')
            exit(-1)


def process_config(args) -> EasyDict:
    """
    Get the json file
    Processing it with EasyDict to be accessible as attributes
    Then set up the logging in the whole program
    Then return the config
    :param args: argument parser output
    :return: config object(namespace)
    """

    # empty config dict
    config = EasyDict()

    # dict for all configs file added to config
    config_path = os.path.join(PROJECT_ROOT, CELL_JSON_PATH) \
        if APPEND_PROJECT_ROOT else CELL_JSON_PATH
    config.cell_dict = get_config_from_json(config_path)

    config_path = os.path.join(PROJECT_ROOT, CELL_TYPE_JSON_PATH) \
        if APPEND_PROJECT_ROOT else CELL_TYPE_JSON_PATH
    config.cell_type_dict = get_config_from_json(config_path)

    config_path = os.path.join(PROJECT_ROOT, HOTEL_JSON_PATH) \
        if APPEND_PROJECT_ROOT else HOTEL_JSON_PATH
    config.hotel_dict = get_config_from_json(config_path)

    config_path = os.path.join(PROJECT_ROOT, HOTEL_UPGRADE_TYPE_JSON_PATH) \
        if APPEND_PROJECT_ROOT else HOTEL_UPGRADE_TYPE_JSON_PATH
    config.hotel_upgrade_type_dict = get_config_from_json(config_path)

    return config
