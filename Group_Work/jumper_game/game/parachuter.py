"""
holds secret word
letters guessed
printing of image for game

"""
import random

class Parachuter:
    def __init__(self) -> None:
        self.words = []
        self.RandomWord = ""
        self.letters = []
        self.print = ""
        self.guessed_letters = []
        self.hp = 5
        self.word_complete = False
        with open("game/wordlist.txt",'r') as f:
            for line in f:
                for word in line.split():
                    self.words.append(word)
        
    def choose_word(self):
        self.RandomWord = random.choice(self.words)
        for x in range(len(self.RandomWord)):
            self.letters.append(self.RandomWord[x])
    
    def create_print(self):
        self.print = ""
        for x in self.letters:
            if x in self.guessed_letters:
                self.print += f" {x.upper()} "
            else:
                self.print += f" _ "
    
    def check_word(self):
        for y in self.letters:
            if y in self.guessed_letters:
                self.word_complete = True
            else:
                self.word_complete = False
                break
