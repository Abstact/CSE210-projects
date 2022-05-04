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

    # main game loop
        # remember to check for taken space
        # handle errors

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
    """
    pass

# run main function
if __name__ == "__main__":
    main()