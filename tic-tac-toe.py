#TIC-TAC-TOE


#Step 1: To print out a board


def display_board(board):
    '''
    docstring: print out the board
    '''

    print("\n"*100)
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


#step 2: write a fncn that takes in a player input and assign their marker as "X" or "O"

def player_input():
    '''
    docstring: player input "X" or "O"
    '''
    marker=" "
    while marker !="X" and marker !="O":
        marker=input("Player 1, choose X or 0: ")
    player1=marker

    if player1=="X":
        player2="0"
    else:
        player2="X"

    return(player1,player2)

#step 3: A fncn that takes in the board object, a marker("X" or "O") and a desired position(1-9) and assigns it to the board

def place_marker(board,marker,position):
    '''
    Docstring: takes the marker and a desired postion and assigns the marker that position
    '''
    board[position]=marker

#Step 4: A fncn that takes in a board and a mark(X or 0) and then checks to see if that mark has won
def win_check(board, mark):
    #win tic tac toe:
    #all rows and check if they all see the same marker
    #repear for columns
    #check if 2 diag
    '''
    Docstring: to check if won or lost
    '''
    for position in board:
        if board[1]==board[2]==board[3]==mark:
            return True
        elif board[4]==board[5]==board[6]==mark:
            return True
        elif board[7]==board[8]==board[9]==mark:
            return True
        elif board[1]==board[4]==board[7]==mark:
            return True
        elif board[2]==board[5]==board[8]==mark:
            return True
        elif board[3]==board[6]==board[9]==mark:
            return True
        elif board[1]==board[5]==board[8]==mark:
            return True
        elif board[3]==board[5]==board[7]==mark:
            return True
        else:
            return False

#Step 5: A fncn that chooses a random module to decide which player goes first

import random

def choose_first():
    '''
    Docstring: who starts first?
    '''
    flip=random.randint(0,1)

    if flip==0:
        return "Player 1"
    else:
        return "Player 2"

#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available

def space_check(board,position):
    '''
    Docstring:  board space check
    '''
    return board[position]==" "

#Step 7: write a function that checks if the board is full

def full_board_check(board):
    '''
    Docstring: full board check
    '''
    for i in range(1,10):
        if space_check(board,i):
            return False

    return True

#Step 8: A fncn that asks for a player's next position and then uses step 6 to see if a free position or not. then return the position for later use

def player_choice(board):
    '''
    Docstring: Next position
    '''

    position=0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position= int(input("Choose a position: (1-9) "))

    return position

#Step 9: Write a function to ask the player if they want to play again (boolean)

def replay():
    '''
    Docstring: want to play again or not
    '''
    return input("Play again? Enter YES or NO " ).lower()=="y"

    

#Step 10: Use while loops and functions to run the game
print("Welcome to Tic Tac Toe!")

while True:
    #set everything up (board->who goes first ->marker choice->outcome):
    the_board=[" "]*10
    player1_marker,player2_marker=player_input()

    turn=choose_first()
    print(turn + " will go first")

    play_game= input("Ready to play? y or no: ")

    if play_game.lower()=="y":
        game_on=True
    else:
        game_on=False


    while game_on:
        if turn=="Player 1":
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)

            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("Player 1 has won!")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("tie game!")
                    break
                else:
                    turn="Player 2"
        else:
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player2_marker,position)

            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("Player 2 has won!")
                game_on=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("tie game!")
                    break
                else:
                    turn="Player 1"


    if not replay():
        break



            



    




        
