import connectfour

def printing_the_board(GameState):
    print('  ', end="")
    print('  '.join(map(lambda x: str(x + 1), range(connectfour.BOARD_COLUMNS))))
    for y in range(connectfour.BOARD_ROWS):
        for x in range(connectfour.BOARD_COLUMNS):
            if GameState.board[x][y]==connectfour.NONE:
                print('  '+'·', end="")
            elif GameState.board[x][y]==connectfour.RED:
                print('  '+'R', end="")
            elif GameState.board[x][y]==connectfour.YELLOW:
                print('  '+'Y', end="")
        print('')

def getString(prompt, options):
    choice = input(prompt).upper().strip()
    while not choice in options:
        print("Invalid input, please enter ", end = "")
        if len(options) == 2:
            print(options[0], "or", options[1])
        else:
            for option in options:
                if option != options[-1]:
                    print(option, end = "," )
                else:
                    print( " or" , option)
        choice = input(prompt).upper().strip()
    return choice

def lets_start_playing():
    print("Below is a representation of the board of connect four tha we will be playing on")
    print("To enter a color into a column just follow the instructions")
    print("Either Drop or Pop by typing 'D' or 'P' respectively.Then press enter.")
    print("Followed by entering the column number in which you would like to do so and pressing Enter again.")
    print("Hope you enjoy this game")
