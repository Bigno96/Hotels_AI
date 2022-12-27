import yaml
import os

from easydict import EasyDict

PROJECT_ROOT = 'D:/Hotels_AI'
APPEND_PROJECT_ROOT = True

CELL_YAML_PATH = 'configs/cell.yaml'
CELL_TYPE_JSON_PATH = 'configs/cell_type.yaml'
HOTEL_YAML_PATH = 'configs/hotel.yaml'
HOTEL_UPGRADE_TYPE_YAML_PATH = 'configs/hotel_upgrade_type.yaml'
GAME_YAML_PATH = 'configs/game.yaml'


def get_config_from_yaml(yaml_file: str
                         ) -> EasyDict:
    """
    Get the config from a yaml file
    :param yaml_file: the path of the config file
    :return: dict of the config file
    """
    # parse the configurations from the config yaml file provided
    with open(yaml_file, 'r') as config_file:
        try:
            return EasyDict(yaml.safe_load(config_file))
        except ValueError:
            print('INVALID YAML file format. Please provide a good yaml file')
            exit(-1)


def process_config(args) -> EasyDict:
    """
    Merge argument parser with various yaml config files
    :param args: argument parser output
    :return: config object
    """
    config = args
    # dict for all configs file added to config
    config_path = os.path.join(PROJECT_ROOT, CELL_YAML_PATH) \
        if APPEND_PROJECT_ROOT else CELL_YAML_PATH
    config.cell_dict = get_config_from_yaml(config_path)

    config_path = os.path.join(PROJECT_ROOT, CELL_TYPE_JSON_PATH) \
        if APPEND_PROJECT_ROOT else CELL_TYPE_JSON_PATH
    config.cell_type_dict = get_config_from_yaml(config_path)

    config_path = os.path.join(PROJECT_ROOT, HOTEL_YAML_PATH) \
        if APPEND_PROJECT_ROOT else HOTEL_YAML_PATH
    config.hotel_dict = get_config_from_yaml(config_path)

    config_path = os.path.join(PROJECT_ROOT, HOTEL_UPGRADE_TYPE_YAML_PATH) \
        if APPEND_PROJECT_ROOT else HOTEL_UPGRADE_TYPE_YAML_PATH
    config.hotel_upgrade_type_dict = get_config_from_yaml(config_path)

    config_path = os.path.join(PROJECT_ROOT, GAME_YAML_PATH) \
        if APPEND_PROJECT_ROOT else GAME_YAML_PATH
    config.game_dict = get_config_from_yaml(config_path)

    return config
