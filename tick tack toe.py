#tick tac toe
#brayden woodard
#11/20

#global constants
x = "X"
o = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

# Functions deffinitions
#####################################################
def display_instructions():
   print( """Display game instructions. to use (display_instructions()"""
    """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.

    You will make your move known by entering a number, 0 - 8. The number
    will correspondto to the board positon as illustrated:

                                \t0 | 1 | 2
                                \t------------
                                \t3 | 4 | 5
                                \t------------
                                \t6 | 7 | 8

    Prepare yourself, human. The ultimate battle is about to begin.
    """
    )

def next_turn(current_turn):
    """this function switches the turn in the game. to use (turn = next_turn(current_turn))"""
    if current_turn == x:
        return o
    else:
        return x

def pieces():
    """Determine if player or computer goes first. to use (computer,human = pieces() )"""
    go_first = ask_yes_no("Do you require the first move? (y/n):"
    if go_first == "y" or go_first == "yes":
        human = x
        computer = o
        print("\nThen take the first move. You will need it.")
    else:
        print("\your bravery will be your undoing. . . I will go first.")
        human = o
        domputer = x
    return computer, human

def ask_yes_no(question):
    """ask a yes or no question and get back a yes or a no
answer. to use (answer = ask_yes_no(questions)) """
    response = None
    while response not in ("y", "n", "yes", "no"):
        response = input(question).lower()
    return response

def new_board():
    """Create a new game board full of empty spaces. to use (board = new_board())"""
    board = [ ]
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Display game board on screen. to use (display_board(board) )"""
    print(str.format("\t{ } | { } | { }",board{0},board{1},board{2}))
    print("\t", "---------")
    print(str.format("\t{ } | { } | { }",board{3},board{4},board{5}))
    print("\t", "---------")
    print(str.format("\t{ } | { } | { }",board{6},board{7},board{8}))

def human_move():
    """get human move to use (move = =human_move()"""
    move = None
    while move == None:
        move = ask_number()
    return move

def ask_number():
    """Ask for a number within a range to use (answer = ask_number(question, low , high))"""
    response = None
    While response not in range(low,high):
        response = int(input(question))
    return response 
    

######################################################


#main game
def main():
    display_instructions()
    turn = x
    computer, human = pieces()
    board = new_board()
    while True:
        display_board(board)
        move = human_move()
        board[move] = human
        turn = next_turn(turn)
     

main()
