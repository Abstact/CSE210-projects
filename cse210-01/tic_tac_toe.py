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
        print()

        # Get user input
        square = int(input(f"{player_mark}'s turn to choose a square (1-9): "))
        while square > 9 or square < 1 or game_grid[square-1] != 0:
            square = int(input("Invalid square, pick again (1-9): "))

        game_grid = turn(game_grid, square, player_turn)

        win = check_win(game_grid)
        # print(f"win - {win}"
        if win != 0:
            break


    # winner printout
    print()
    view_grid(game_grid)
    winner = check_win(game_grid)
    if winner == 0:
        print("It's a tie!")
    elif winner == 1:
        print("X's victory!")
    elif winner == 2:
        print("O's win!")

    print("Thanks for playing!")

def view_grid(grid):
    """
    Prints out the current grid
    """
    # set up each row
    squares = ['1','2','3','4','5','6','7','8','9']
    for i in range(0,9):
        if grid[i] == PLAYER_O_INDEX:
            squares[i] = 'O'
        if grid[i] == PLAYER_X_INDEX:
            squares[i] = 'X'

    #print out rows
    print(f"     {squares[0]}|{squares[1]}|{squares[2]}")
    print("     -+-+-")
    print(f"     {squares[3]}|{squares[4]}|{squares[5]}")
    print("     -+-+-")
    print(f"     {squares[6]}|{squares[7]}|{squares[8]}")

def turn(grid, square, player_num):
    """
    changes the number in the grid
    """
    grid[square-1] = player_num
    return grid

def check_win(grid):
    """
    check the grid for a win
    returns:
        0 for no win
        1 for X win
        2 for O win
    """
    # check rows
    if grid[0] == grid[1] == grid[2] and grid[0] != 0:
        return grid[0]
    if grid[3] == grid[4] == grid[5] and grid[3] != 0:
        return grid[3]
    if grid[6] == grid[7] == grid[8] and grid[6] != 0:
        return grid[6]

    # check columns
    if grid[0] == grid[3] == grid[6] and grid[0] != 0:
        return grid[0]
    if grid[1] == grid[4] == grid[7] and grid[1] != 0:
        return grid[1]
    if grid[2] == grid[5] == grid[8] and grid[2] != 0:
        return grid[2]

    # check diagnals
    if grid[0] == grid[4] == grid[8] and grid[4] != 0:
        return grid[4]
    if grid[2] == grid[4] == grid[6] and grid[4] != 0:
        return grid[4]

    return 0

# run main function
if __name__ == "__main__":
main()