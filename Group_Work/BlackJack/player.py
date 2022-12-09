import random
from input_service import Input

class Player():
    """
        Class that contains all the methods relating to the player
        Data needed:
            A count of the wins
            Cards held

        Methods needed:
            deal()
            player_turn()
            reset()

    """
    
    
    def __init__(self):
        self.win_count = 0
        self.cards = []
        card_total = 0
        self.input = Input()

    def deal(self):
        """
            Method that adds a card to self
        """
        self.cards.append(random.randint(1,52))

    def player_turn(self):
        pass

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
            card_total = 0
            return
        
        # Check raw sum
        card_total = 0
        for i in 
