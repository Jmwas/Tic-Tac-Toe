# The TIC TAC TOE Game
import random
import os

def clear():
    os.system('cls')

# A function that can print out a board.
# Each index 1-9 corresponds with a number on a number pad.
def display_board(board):
    clear()
    print('--------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('--------')

# function that uses the random module to randomly decide which player goes first
def choose_first():
    return 'player ' + str(random.randint(1, 2))

# A function that can take in a player input and assign their marker as 'X' or 'O'
def player_input():
    marker = ''

    while marker != 'x' and marker != 'o':
        marker = input("Please choose x or o: ").lower()

    player1 = marker

    if player1 == 'x':
        player2 = 'o'
    else:
        player2 = 'x'

    return player1, player2

# Function that takes in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the board
def place_marker(board, marker, position):
    board[position] = marker

# function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or
            (board[4] == board[5] == board[6] == marker) or
            (board[7] == board[8] == board[9] == marker) or
            (board[7] == board[4] == board[1] == marker) or
            (board[8] == board[5] == board[2] == marker) or
            (board[9] == board[6] == board[3] == marker) or
            (board[1] == board[5] == board[9] == marker) or
            (board[7] == board[5] == board[3] == marker))

# Check whether a space on the board is freely available. Returns True if available otherwise False
def space_check(board, position):
    return board[position] == ' '

# Check if the board is full and returns a boolean value. True if full, False otherwise
def full_board_check(board):
    for i in range(1, 10):
        # check if board is full
        if space_check(board, i):
            return False
    return True # Board is full

# Ask for a player's next position (as a number 1-9) and then uses space_check() to check if free position.
# If it is, then return the position for later use.
def player_choice(board):
    position = 0

    while position not in range(1,11) or not space_check(board, position):
        position = int(input('Please select a position from 1 - 9: '))
    return position

print('Welcome to Tic Tac Toe')

while True:
    clear()  # Reset the board
    theBoard = [' '] * 10
    play_game = input('Do you want to play? Y or N ').lower()
    if play_game == 'y':
        game_on = True
    else:
        print("Good Bye!!!")
        exit()

    turn = choose_first()
    print(turn + ' will go first')
    player1_marker, player2_marker = player_input()

    while game_on:
        if turn == 'Player 1': # Player1's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations Player 1! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations Player 2! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

