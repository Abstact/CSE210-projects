from dealer import Dealer
from player import Player
from terminal_service import Terminal
from input_service import Input

class Director():
    """
        Class that controls the game
    """
    def __init__(self):
        self.playing = True #self.playing - Determines whether or not the game is being played or if the player has ended the game
        self.cards_dealt = False #self.cards_dealt - Prevents the while loop for dealing cards twice
        self.player = Player() #Remaining variables are just initializing classes
        self.dealer = Dealer()
        self.terminal = Terminal()
        self.input = Input()
    
    def start_game(self):
        """
            Initializes and loops the game
        """
        self.terminal.intro() #Welcomes the user with a message that welcomes the user and presents the rules. You can determine whether or not the game waits for the user to read the rules
        while self.playing:
            self.deal_cards()
            self.take_turns()
            self.results()
            self.reset()
    
    def deal_cards(self):
        """
            Has the dealer and the player both deal their own cards. Random number generator picks a card and assigns the proper color and number for each class.
        """
        if self.cards_dealt:
            return
        if not self.playing:
            return

        self.player.deal() #Use terminal service to display the cards after each deal
        self.dealer.deal()
    
    def take_turns(self):
        """
            The player takes their turn using the input service for logic on possible options. Player keeps on going until they get 21 or above. Dealer keeps going until AI tells it to stop. Uses terminal to show cards and value.
        """
        if not self.playing:
            return

        self.player.player_turn()
        self.dealer.dealer_turn()
    
    def results(self):
        """
            Logic on who wins the game. Uses terminal to display appropriate message
        """
        if not self.playing:
            return

        if self.player.card_total > self.dealer.card_total:
            self.terminal.player_win()
        elif self.player.card_total < self.dealer.card_total:
            self.terminal.dealer_win()
        elif self.player.card_total == self.dealer.card_total:
            self.terminal.tie()

    def reset(self):
        """
            Ends game and asks player if they'd like to continue the game.
        """
        if not self.playing:
            return
        
        if self.input.keep_playing():
            self.dealer.reset() #Removes all stored card values
            self.player.reset()
            self.cards_dealt = False
        else:
            self.playing = False
            self.terminal.goodbye() #Displays goodbye message