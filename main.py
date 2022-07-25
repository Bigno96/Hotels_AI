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

    # game_manager = GameManager(config)

if __name__ == '__main__':
    __spec__ = None
    main()


