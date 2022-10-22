"""
Terminal Service
Variables: None
Functions:
    Rules prompt
        - prints out rules for game
    print_word(string)
        -
    print_guy(int)
        -
    game_over()
        -
    game_won(string)
        -

"""
import parachuter

class Terminal_service:
    def Rules_prompt():
        print("Welcome to Jumper!")
        print("You are tasked with guessing a word one letter at a time. Be careful though, as each wrong letter will take some of your parachute away! Too many wrong guesses will cause you to make a quicker landing than was planned.")

    
    def print_word(word):
        print(word)

    def print_guy(hp):
        parachuter.printState(hp)

    def game_over(word):
        print("GAME OVER")
        print("Too many wrong guesses")
        print("The word was " + word)

    def game_won(word):
        print("CONGRATS! You won!")
        print("The word was " + word)

