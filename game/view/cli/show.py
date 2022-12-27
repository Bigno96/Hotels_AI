from game.model.board import Board

def show_board(board : Board
               ) -> str:
    # dict of player pos
    _player_pos = {
        val: key
        for key, val in self.__position_trace.items()
    }

    def _cell_repr(cell_id: int) -> str:
        _cell = self.__cell_list[cell_id]   # find the cell
        # if the cell is occupied
        if _cell in _player_pos.keys():
            # for starting cell, get the color of the first player available
            return colorize(input_string=f'|{cell_id:02}|',
                            fg=self.__player_color_map[_player_pos[_cell]])
        return f'|{cell_id:02}|'

    '''split cells into 4 quadrants'''
    top_cell = [self.__cell_list[i] for i in range(-1, 10)]
    bot_cell = [self.__cell_list[i] for i in range(25, 14, -1)]
    right_cell = [self.__cell_list[i] for i in range(10, 15)]
    left_cell = [self.__cell_list[i] for i in range(30, 25, -1)]

    '''cells representation'''
    top_row = '\t\t'.join([_cell_repr(c.get_id()) for c in top_cell])
    bot_row = '\t\t'.join([_cell_repr(c.get_id()) for c in bot_cell])
    right_col = [_cell_repr(c.get_id()) for c in right_cell]
    left_col = [_cell_repr(c.get_id()) for c in left_cell]

    '''hotel representation'''
    upper_top_hotel = '\t  '*5 + ('Boomerang' + '\t  ')*5 + '\t  '*9 + 'President'

    '''color legend'''
    _repr = 'Players: '
    for pl, clr in self.__player_color_map.items():
        _repr += colorize(input_string=pl.get_name(), fg=clr) + ' '
    _repr += '\n\n'

    '''actual board'''
    _repr += f'{upper_top_hotel}\n\n'
    _repr += f'{top_row}\n\n'
    # transpose to put column in place
    for item in zip(left_col, right_col):
        _repr += item[0] + '\t'*29 + item[1] + '\n\n'    # format and tabulate
    _repr += bot_row

    return _repr