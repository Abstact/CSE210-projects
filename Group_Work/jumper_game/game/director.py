from Group_Work.jumper_game.game.parachuter import Parachuter
from Group_Work.jumper_game.game.terminal_service import Terminal_service
from Group_Work.jumper_game.game.user import User

'''
Code Explination:
Main will call director to start the game

play_game():
Parachuter will be called to create the word.
This word will be broken up into individual letters all placed into a list. We can use this list to check if the letter guessed is in the word.
We will create a loop that will continue until the parachuter has HP of 0 or the word is guessed

print_parachute():
Parachuter is called to create the string of blanks and letters based of what the user has guessed.
Terminal will print off the string previously created and the guy based of his hp

get_inputs():
User is called to collect guess from user. User makes sure the guess is only one letter and returns it lowercase.
The guess is added to the list of guessed letters
If the guess is incorrect, the hp is reduced by one

clean_up():
Check_word is used to see if all the letters have been guessed by the user. Sets 'word_complete' to true if complete
If the HP falls bellow 0, play is ended and terminal is called to print game over
If the word is complete, play is ended. The completed word, a happy parachuter, and congrats are all printed out.
'''


class Director:

    def __init__(self) -> None:
        self.playing = True
        self.parachuter = Parachuter()
        self.terminal = Terminal_service()
        self.user = User()

    def play_game(self):
        self.parachuter.choose_word() #Chooses a word in the parachuter class. Try breaking this word up into indiviual letters in a list
        while self.playing: #Loops until user wins or loses
            self.print_parachuter()
            self.get_inputs()
            self.clean_up()

    def print_parachuter(self): #Prints all information
        if not self.playing:
            return
        self.parachuter.create_print() #This creates a string for terminal to use that has guessed letters filled in and missing ones left as blank
        self.terminal.print_word(self.parachuter.print) #This prints off the string created by parachuter
        self.terminal.print_guy(self.parachuter.hp) #Prints the parachuter himself. It will update based off the "hp" or health the parachuter has
    
    def get_inputs(self):
        if not self.playing:
            return
        guess = self.user.get_input() #Returns the letter the user guessed. Make sure the user only has one letter
        self.user.guessed_letters.append(guess)
        if guess not in self.parachuter.letters:
            self.parachuter.hp -= 1
    
    def clean_up(self):
        if not self.playing:
            return
        self.parachuter.check_word()
        if self.parachuter.hp <= 0: #Ends the game if the parachuter has lost all of its parachute
            self.playing = False
            self.terminal.game_over(self.parachuter.word)
        elif self.parachuter.word_complete: #Ends game if boolean valiable 'word_complete' is true
            self.playing = False
            self.terminal.game_won(self.parachuter.word)
