# Author: J.Hadida (jhadida87 at googlemail)

class PlayerColorEnum:
    Red = 'r'
    Yellow = 'y'
    Green = 'g'
    Blue = 'b'
    Magenta = 'm'
    Cyan = 'c'
    White = 'w'

COLCODE = {
    'k': 0,  # black
    'r': 1,  # red
    'g': 2,  # green
    'y': 3,  # yellow
    'b': 4,  # blue
    'm': 5,  # magenta
    'c': 6,  # cyan
    'w': 7,  # white
}

FMTCODE = {
    'b': 1,  # bold
    'f': 2,  # faint
    'i': 3,  # italic
    'u': 4,  # underline
    'x': 5,  # blinking
    'y': 6,  # fast blinking
    'r': 7,  # reverse
    'h': 8,  # hide
    's': 9,  # strikethrough
}


def colorize(input_string,
             fg=None,
             bg=None,
             style=None
             ) -> str:
    """
    Color-printer.
        cprint( 'Hello!' )                                  # normal
        cprint( 'Hello!', fg='g' )                          # green
        cprint( 'Hello!', fg='r', bg='w', style='bx' )      # bold red blinking on white
    List of colors (for fg and bg):
        k   black
        r   red
        g   green
        y   yellow
        b   blue
        m   magenta
        c   cyan
        w   white
    List of styles:
        b   bold
        i   italic
        u   underline
        s   strikethrough
        x   blinking
        r   reverse
        y   fast blinking
        f   faint
        h   hide
    """

    # properties
    props = []
    if style:
        props = [FMTCODE[s] for s in style]
    if fg:
        props.append(30 + COLCODE[fg])
    if bg:
        props.append(40 + COLCODE[bg])

    # display
    props = ';'.join([str(x) for x in props])
    if props:
        return f'\x1b[{props}m{input_string}\x1b[0m'
    else:
        return input_string
