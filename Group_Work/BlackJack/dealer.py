# Some of the intrsutions are taken from (https://1883magazine.com/how-to-play-blackjack-online-step-by-step-guide/)

import random
from terminal_service import Terminal


class Dealer():
    """
        Class that contains all the methods relating to the Dealer
        Data needed:
            A count of the wins
            Cards held
            Total of the cards held
            Minimum total to stand at

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
        self.min_stand = 18 #minimum number the dealer can stand on
        self.terminal = Terminal()

    def deal(self):
        """
            Method that adds a card to self
        """
        self.cards.append(random.randint(1,52))

    def dealer_turn(self):
        """
            Method that goes through the dealer turn. If under min_stnad, then hit until bust
        """
        
        while (self.card_total < 0) and (self.card_total > 21):
            # Display cards and total
            for i in self.cards:
                self.terminal.show_card(i)
            print(f"Total: {self.card_total}")

            # hit or stand
            if self.card_total < self.min_stand:
                self.deal()
            else:
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
            self.card_total += int(i / 4) + 1
            # card number is one more than the raw value divided by 4
        
        # if bust, check for aces, subtract 10 if needed
        if self.card_total > 21:
            for i in self.cards:
                if int(i / 4) == 0:
                    self.card_total -= 10
        
        # if still bust, set to -1
        if self.card_total > 21:
            self.card_total = -1