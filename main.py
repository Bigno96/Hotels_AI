"""
Main execution file for HOTEL AI

-Capture the config file
-Process the json configs passed
-Create a game instance
-Play the game
"""

import argparse
from utils.config import process_config


def main():
    """
    Main function
    Parses argument
    Create and play a game
    """

    # set up argument parser to read input arguments
    arg_parser = argparse.ArgumentParser(description="")

    # get the argument from the console
    args = arg_parser.parse_args()

    # parse the config json file
    config = process_config(args)

    # checking consistency
    n_players = config.game_dict.n_players
    dict_player_list = config.game_dict.player_list
    if len(dict_player_list) != n_players:  # number of players not matching the list of players
        print(f'Different number of players declared. Expected {n_players}, got {len(dict_player_list)}.')
        exit(-1)

    # game_manager = GameManager(config)

if __name__ == '__main__':
    main()


