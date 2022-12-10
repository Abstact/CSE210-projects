# Some of the intrsutions are taken from (https://1883magazine.com/how-to-play-blackjack-online-step-by-step-guide/)

from termcolor import cprint, colored
import random
import os

os.system('color')

class Terminal():
    """
        Class that controls the terminal service
    """
    def __init__(self) -> None:
        pass
        

    def intro(self):
        """
            Shows a welcome message
        """
        print("Welcome to Blackjack!")

        def ask():
            """
                Asks the user if they would want to read the instructions.
            """
            read_instructions = input(f"Do you want to read the instructions(Y/N)?\n\t→ ")
            if read_instructions.upper() == "Y":
                print("\nHow to Play:")
                print("\n→ You get 2 cards dealt to you")
                print("→ Decide when you want to 'HIT'\n\t-This increases the value of your hand\n\t-If you cross 21 and go bust, you lose your money")
                print("\t-You have to make sure that you have healthy hand\n\t and that if it cross values of 16 or 17, you should \n\t decide if you are willing to take a risk")
                print("→ Decide when you want to 'STAND'\n\t-When you are satisfied with your hand, choose to STAND")
                print("→ The Outcome\n\t-You WIN if the value of the cards in your \n\t hand are higher than the dealers or is equal to 21")
                print("\t- If the value of your hand is lower than the \n\t dealers or cross 21, you LOSE")

            elif read_instructions.upper() == "N":
                print("I guess you're ready. Let's Go!")

            else:
                print("Please enter either Y or N")
                ask()
        ask()

    def player_win(self):
        """
            Display random player won messages
        """
        winning_statements = ["Heh, I knew you'd win!", 
                            "Didn't doubt you a bit", 
                            "Wow, you're so lucky!", 
                            "Looks like luck's on your side today!", 
                            "You won!"]

        print(random.choice(winning_statements))

    def dealer_win(self):
        """
            Display random player lost messages
        """
        losing_statements = ["Better luck next time!",
                            "Too bad",
                            "You can do better!",
                            "You lost"]

        print(random.choice(losing_statements))

    def tie(self):
        """
            Display random tie messages
        """
        tie_statements = ["It's a tie!",
                        "You just tied with the dealer!",
                        "It's a draw!",
                        "That was tense, yet a draw"]
        
        print(random.choice(tie_statements))

    def score(self, player_score, dealer_score):
        """
            Displays both scores

            Args:
                player_score
                dealer_score
        """
        print(f"Your score: {player_score}")
        print(f"Dealer's Score: {dealer_score}")

    def goodbye(self):
        """
            Goodbye message
        """
        print("Thank you for playing Blackjack with us!\nSee ya again next time!")

    def show_card(self, cards):
        """
            Displays the card in the terminal.

            Arg(s):
                cards: A random number from 1-52

            - (1) Hearts: Red
            - (2) Clubs: Blue
            - (3) Spades: Green
            - (4) Diamonds: Yellow
            
        """
        card_number = int(cards / 4)
        card_color = int(cards % 4)

        card_number_display = [2,3,4,5,6,7,8,9]

        if card_number in card_number_display:
            card_number += 1

        if card_number == 1:
            card_number = "A"

        if card_number == 11:
            card_number = "J"
        
        if card_number == 12:
            card_number = "Q"

        if card_number == 13:
            card_number = "K"

        # Identify whether card value has 1 or 2 digits to adjust display
        if len(str(card_number)) == 1:
            display = f" ___ \n|   |\n| {card_number} |\n|___|"
        elif len(str(card_number)) == 2:
            display = f" ____ \n|    |\n| {card_number} |\n|____|"

        # Identify the card color value to display
        if card_color == 0: 
            color = "red"         # Hearts
        elif card_color == 1: 
            color = "blue"        # Clubs
        elif card_color == 2: 
            color = "green"       # Spades
        elif card_color == 3: 
            color = "yellow"      # Diamonds

        cprint(display, color)

    # show_card(random.randint(1,13), random.randint(1,4))      # Test if show_card function works
    # show_card(random.randint(1,52))