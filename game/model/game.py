"""
Contains Game class
Game is the main model class, where every model information is grouped
"""
import game.model.player as player
import game.model.hotel as hotel
import game.model.board as board

from easydict import EasyDict


class Game:
    """
    Game class
    """

    def __init__(self,
                 config: EasyDict):
        """
        Build Game reading configuration
        :param config: global config dictionary
        """
        # dict to track players status
        self.__player_list: dict[str: player.Player] = {
            p.name:
                player.AiPlayer(name=p.name) if p.is_ai
                else player.HumanPlayer(name=p.name)
            for p in config.game_dict.player_list
        }
        # board for the game
        self.__board: board.Board = board.Board(config=config,
                                                player_list=self.__player_list.values())
        # dict to track hotels status
        self.__hotel_list: dict[str: hotel.Hotel] = {
            hotel_name: hotel.Hotel(name=hotel_name, config=config)
            for hotel_name in config.hotel_dict.keys()
        }

    def __repr__(self):
        _repr = 'Game State: \n\n'
        # player state
        for pl in self.__player_list.values():
            _repr += f'{pl}\n'
        # board state
        _repr += f'{self.__board}'

        return _repr

    def remove_player(self,
                      p: player.Player = None,
                      name: str = None
                      ) -> None:
        """
        Remove a player from the game
        In case both name and player.Player are specified, player.get_name overrides name
        :param p: Player to remove
        :param name: name of the player to remove
        :raise AssertionError if neither player nor name are specified
        """
        assert p or name, f'No player to remove'
        if p:
            name = p.get_name()
        if name in self.__player_list.keys():
            del self.__player_list[name]

    def get_player(self,
                   name: str
                   ) -> player.Player:
        """
        Get a player in the game given the name
        :param name: name of the player to be found in the game
        :return: player instance
        :raise IndexError if player is not in the game
        """
        if name not in self.__player_list.keys():
            raise IndexError(f'Could not find Player {name} in the game')
        return self.__player_list[name]

    def get_hotel(self,
                  name: str
                  ) -> hotel.Hotel:
        """
        Get a hotel in the game given the name
        :param name: name of the hotel to be found in the game
        :return: hotel instance
        :raise IndexError if hotel is not in the game
        """
        if name not in self.__hotel_list.keys():
            raise IndexError(f'Could not find Hotel {name} in the game')
        return self.__hotel_list[name]

    def get_board(self) -> board.Board:
        """
        :return: board of the game
        """
        return self.__board

    def get_player_list(self) -> dict[str: player.Player]:
        """
        :return: player list of the game
        """
        return self.__player_list

    def get_hotel_list(self) -> dict[str: hotel.Hotel]:
        """
        :return: hotel list of the game
        """
        return self.__hotel_list