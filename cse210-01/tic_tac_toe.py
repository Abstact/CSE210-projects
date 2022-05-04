"""
JR Ogden
Tic Tac Toe game - CSE210 project 1

Gameplay:
    3x3 grid of squares
    2 players: 'x' and 'o'
    take turns marking squares
    first to three in a row wins

functions:
    main()
        main game loop and input
    view_grid(grid)
        prints grid
    turn(player_num, square)
        replaces that square with an 'x' or an 'o'
    check_win()
        check current grid for a win condition
        returns player num of winner, or draw
"""

# global variables
PLAYER_X_INDEX = 1
PLAYER_O_INDEX = 2

def main():
    """
    Starts a game of Tic Tac Toe
    Prints out directions for play
    Loops through the different 
    """
    game_grid = [0,0,0,0,0,0,0,0,0]

    # Gameplay directions
    print("The goal of the game is to get three in a row. To play, simply type the number of the square you would like to place your marker.")

    # main game loop
        # remember to check for taken space
        # handle errors
    player_turn = 0
    player_mark = ''
    for turn_num in range(1,10):
        if turn_num%2 == 0:
            player_turn = PLAYER_O_INDEX
            player_mark = 'O'
        else:
            player_turn = PLAYER_X_INDEX
            player_mark = 'X'

        #print(turn_num)
        view_grid(game_grid)

        # Get user input
        square = int(input(f"{player_mark}'s turn to choose a square (1-9): "))
        while square > 9 or square < 1 or game_grid[square] != 0:
            square = int(input("Invalid square, pick again (1-9): "))

        turn(game_grid, square, player_turn)

        if check_win(game_grid) != 0:
            turn_num = 10


    # winner printout

def view_grid(grid):
    """
    Prints out the current grid
    """
    pass

def turn(grid, square, player_num):
    """
    changes the number in the grid
    """
    pass

def check_win(grid):
    """
    check the grid for a win
    returns:
        0 for no win
        1 for X win
        2 for O win
    """
    pass

# run main function
if __name__ == "__main__":
    main()