import random

def main():

    play = input("Do you want to play High/Low? Y or N? ")
    
    while play == "y" or "Y":

        print("The current card is: ")
        guess = input("Guess H for high or L for low." )
        if guess == "h" or "H":
            if """Needs a value""" > """Needs a value""":
                print("Congratulations, you guessed correctly!")
                play = input("Play again? Y or N? ")

            if """Needs a value""" < """Needs a value""":
                print("Unfortunately, you lost!")
                play = input("Play again? Y or N? ")

        if guess == "l" or "L":
            if """Needs a value""" > """Needs a value""":
                print("Unfortunately, you lost!")
                play = input("Play again? Y or N? ")

            if """Needs a value""" < """Needs a value""":
                print("Congratulations, you guessed correctly!")
    else:
        print("Game Over! Thank you for playing.")

    """Pressing N doesn't end the game"""
    
# This is Chris's Comment
class Director:
    '''
    insert class comment here
    '''
    #THIS IS A COMMENT 
    def __init__(self):
        pass

class Card:
    def __init__(self):
        self.lastCard = random.randrange(1,13)
    # testing if we can remember the last card
    """
    code to be added by JR later
    """
    def getCard():
        newCard = random.randrange(1,13)
        # lastCard = newCard
        return newCard

if __name__ == "__main__":
    main()