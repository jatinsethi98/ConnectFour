import connectfour
import collections
import common_functions

GameState = collections.namedtuple('GameState', ['board', 'turn'])



def introduction():
    print("We have two players to begin with Red and Yellow")
    print("We will start with player Red")

    
def starting_new_game():
    raw_board_and_turn = connectfour.new_game()
    raw_board = raw_board_and_turn.board
    raw_turn = raw_board_and_turn.turn

    return GameState(board = raw_board, turn = raw_turn)
        


def dropping(game_state: GameState):
    while True:
        try:
            column_number=int(input("\nEnter the column number in which you would like to drop: "))-1
            if column_number > 7 or column_number <= -1:
                print("Please enter a valid column number. Column",column_number,"does not exit.")
            else:
                game_state=connectfour.drop(game_state, column_number)
                return game_state

        except ValueError:
            print("Please enter a valid value integer")
        except connectfour.InvalidMoveError:
            print("Column is already filled.")


def popping(game_state: GameState):
    while True:
        try:
            column_number=int(input("\nEnter the column number in which you would like to pop: "))-1
            if column_number > 7 or column_number <= -1:
                print("Please enter a valid column number. Column",column_number,"does not exit.")
            else:
                game_state=connectfour.pop(game_state, column_number)
                return game_state

        except ValueError:
            print("Please enter a valid value integer")
        except connectfour.InvalidMoveError:
            print("Piece cannot be popped or the column is empty.")


def giving_options():
    return common_functions.getString("What would you like to do? Drop(D) or Pop(P): ",['D','P'])
##    dp=input("\nWhat would you like to do? Drop(D) or Pop(P): ").upper().strip()
##    if dp != "D" and dp != "P":
##        print("Invalid input. Enter 'D' or 'P'")
##        giving_options()
##    else:
##        return dp
    
def user_interface():
    common_functions.lets_start_playing()
    introduction()
    game_state = starting_new_game()
    common_functions.printing_the_board(game_state)
    game_state=dropping(game_state)
    common_functions.printing_the_board(game_state)
    while True:
        try:
            new=game_state.turn
            if new == 1:
                new="Red"
            else:
                new="Yellow`"
            print("\nIt is "+str(new)+"'s turn now")
            dp=giving_options()
            if dp == "D":
                game_state = dropping(game_state)
                common_functions.printing_the_board(game_state)
            else:
                game_state = popping(game_state)
                common_functions.printing_the_board(game_state)
            if connectfour.winner(game_state) == connectfour.NONE:
                pass
            else:
                Winner=connectfour.winner(game_state)
                print("\n\nCONGRATULATIONS!",Winner,"has won the game!")
                break
        except connectfour.GameOverError:
            Winner=connectfour.winner(game_state)
            if Winner == 1:
                Winner="Red"
            else:
                Winner="Yellow`"
            print("\n\nCONGRATULATIONS!",Winner,"has won the game!")
            break

    
user_interface()
