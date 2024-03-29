# Some of the intrsutions are taken from (https://1883magazine.com/how-to-play-blackjack-online-step-by-step-guide/)

import random
from input_service import Input
from terminal_service import Terminal

class Player():
    """
        Class that contains all the methods relating to the Player
        Data needed:
            A count of the wins
            Cards held
            Total of the cards held

        Methods needed:
            deal()
            dealer_turn()
            reset()
            update_count()
    """
    
    def __init__(self):
        self.win_count = 0
        self.cards = []
        self.card_total = 0
        self.input = Input()
        self.terminal = Terminal()

    def deal(self):
        """
            Method that adds a card to self
        """
        self.cards.append(random.randint(1,52))
        self.update_count()

    def player_turn(self):
        """
            Method that goes through the player turn. Shows the cards, then asks player to hit/stand until bust
        """
        
        while (self.card_total > 0) and (self.card_total < 21):
            # Display cards and total
            for i in self.cards:
                self.terminal.show_card(i)
            print(f"Total: {self.card_total}")

            # Ask for hit/stand
            self.input.hit_stand()
            if self.input.hit:
                self.deal()
            else:
                #no more cards desired. Update count and stop method
                self.update_count()
                return

            self.update_count()


    def reset(self):
        """
            Sets cards to none, total to none
        """
        self.cards = []
        self.card_total = 0
    
    def update_count(self):
        """
            Reads the value of all cards (be careful with aces)
            set self.card_total to current value
                if bust, set to -1
        """
        if len(self.cards) == 0:
            self.card_total = 0
            return
        
        # Check raw sum
        self.card_total = 0 #fresh check each time
        for i in self.cards:
            card = int(i / 4) + 1
            if card == 1:
                self.card_total += 11
            elif card >= 11:
                self.card_total += 10
            else:
                self.card_total += card
            # card number is 11 if Ace, or 10 if a Royal, or the card value if 2-10
        
        # if bust, check for aces, subtract 10 if needed
        if self.card_total > 21:
            for i in self.cards:
                if int(i / 4) == 0 & self.card_total > 21:
                    self.card_total -= 10
        
        # if still bust, set to -1
        if self.card_total > 21:
            self.card_total = -1