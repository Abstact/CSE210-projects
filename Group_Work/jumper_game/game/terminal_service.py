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

class Terminal_service:
    def Rules_prompt():
        print("Welcome to Jumper!")
        print("You are tasked with guessing a word one letter at a time. Be careful though, as each wrong letter will take some of your parachute away! Too many wrong guesses will cause you to make a quicker landing than was planned.")

    def print_word(self, word):
        print(word)

    def print_guy(self, hp):
        myString = ""

        if hp == 5:
            myString = "________      "
            myString  = myString + '\n' + "|      ___      "
            myString  = myString + '\n' + "|     /   \     "
            myString  = myString + '\n' + "|      ---      "
            myString  = myString + '\n' + "|      \  /     "
            myString  = myString + '\n' + "|       \/      "
            myString  = myString + '\n' + "|       0       "
            myString  = myString + '\n' + "|     / | \     "
            myString  = myString + '\n' + "|      / \      "
            myString  = myString + '\n' + "|               "
            myString  = myString + '\n' + "|   ^^^^^^^^^   "
        elif hp == 4:
            myString  = "________      "
            myString  = myString + '\n' + "|     /   \     "
            myString  = myString + '\n' + "|      ---      "
            myString  = myString + '\n' + "|      \  /     "
            myString  = myString + '\n' + "|       \/      "
            myString  = myString + '\n' + "|       0       "
            myString  = myString + '\n' + "|     / | \     "
            myString  = myString + '\n' + "|      / \      "
            myString  = myString + '\n' + "|               "
            myString  = myString + '\n' + "|   ^^^^^^^^^   "
        elif hp == 3:
            myString  = "________      "
            myString  = myString + '\n' + "|      ---      "
            myString  = myString + '\n' + "|      \  /     "
            myString  = myString + '\n' + "|       \/      "
            myString  = myString + '\n' + "|       0       "
            myString  = myString + '\n' + "|     / | \     "
            myString  = myString + '\n' + "|      / \      "
            myString  = myString + '\n' + "|               "
            myString  = myString + '\n' + "|   ^^^^^^^^^   "
        elif hp == 2:
            myString  = "________      "
            myString  = myString + '\n' + "|      \  /     "
            myString  = myString + '\n' + "|       \/      "
            myString  = myString + '\n' + "|       0       "
            myString  = myString + '\n' + "|     / | \     "
            myString  = myString + '\n' + "|      / \      "
            myString  = myString + '\n' + "|               "
            myString  = myString + '\n' + "|   ^^^^^^^^^   "
        elif hp == 1:
            myString = "________      "
            myString  = myString + '\n' + "|       \/      "
            myString  = myString + '\n' + "|       0       "
            myString  = myString + '\n' + "|     / | \     "
            myString  = myString + '\n' + "|      / \      "
            myString  = myString + '\n' + "|               "
            myString  = myString + '\n' + "|   ^^^^^^^^^   "
        else:
            myString = "________      "
            myString  = myString + '\n' + "|       X       "
            myString  = myString + '\n' + "|     / | \     "
            myString  = myString + '\n' + "|      / \      "
            myString  = myString + '\n' + "|               "
            myString  = myString + '\n' + "|   ^^^^^^^^^   "
        print(myString)

    def game_over(self, word):
        print("GAME OVER")
        print("Too many wrong guesses")
        print("The word was " + word)

    def game_won(self, word):
        print("CONGRATS! You won!")
        print("The word was " + word)

