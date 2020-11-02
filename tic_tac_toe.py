
def main ():
    a = player_move()
    print("="*len(a))
    print(a)
    print("="*len(a))

BOARD = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ','6': ' ',
         '7': ' ', '8': ' ', '9': ' '}
SYMBOLS = ['o', 'x']
FREE_FIELD = list(range(1,10))

def print_board ():
    '''Visualisation of actual Board'''
    global BOARD
    SPLITTER = '-' * 11
    print(f'''{SPLITTER}
{BOARD['7']:^3}|{BOARD['8']:^3}|{BOARD['9']:^3}
{SPLITTER}
{BOARD['4']:^3}|{BOARD['5']:^3}|{BOARD['6']:^3}
{SPLITTER}
{BOARD['1']:^3}|{BOARD['2']:^3}|{BOARD['3']:^3}
{SPLITTER}''')


def if_win ():
    '''Check if player win '''
    global BOARD
    if BOARD.get('1') == BOARD.get('2') == BOARD.get('3') == ('o' or 'x'):
        return True
    elif BOARD.get('4') == BOARD.get('5') == BOARD.get('6') == ('o' or 'x'):
        return True
    elif BOARD.get('7') == BOARD.get('8') == BOARD.get('9') == ('o' or 'x'):
        return True
    elif BOARD.get('1') == BOARD.get('4') == BOARD.get('7') == ('o' or 'x'):
        return True
    elif BOARD.get('2') == BOARD.get('5') == BOARD.get('8') == ('o' or 'x'):
        return True
    elif BOARD.get('3') == BOARD.get('6') == BOARD.get('9') == ('o' or 'x'):
        return True
    elif BOARD.get('3') == BOARD.get('5') == BOARD.get('7') == ('o' or 'x'):
        return True
    elif BOARD.get('1') == BOARD.get('5') == BOARD.get('9') == ('o' or 'x'):
        return True
    else:
        return False


def put_in_board (player):
    '''Player input.
     Check if player input is correct.
     Update board'''
    global BOARD
    global FREE_FIELD

    try:
        try_again = True
        while try_again:
            player_input = int(input((f'Player {SYMBOLS[player]} |'
                                      f' Please enter your move number '
                                      f'(1-9): ')))
            if player_input not in FREE_FIELD:
                print('Input only int 1-9.')
                try_again = True
            else:
                try_again = False
        FREE_FIELD.remove(player_input)
        BOARD[str(player_input)] = SYMBOLS[player]
        return BOARD

    except (ValueError):
        print('Input only int 1-9.')
        return 'again'


def player_move ():
    '''Change players,
    return which player win'''
    turns = 0
    while turns < 9:
        player = turns % 2
        a = put_in_board(player)
        if a == 'again':
            turns += 0
        else:
            turns += 1
            print_board()
            if if_win() == True:
                return f'Player {SYMBOLS[player]} win.'
    else:
        return f'Nobody win'

if __name__ == '__main__':
    main()