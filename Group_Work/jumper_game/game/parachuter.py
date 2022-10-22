"""
holds secret word
letters guessed
printing of image for game

"""
import random

class Parachuter:
#This class is in charge of managing the word as well as keeping track of the health of the parachuter

    def __init__(self) -> None:
        self.words = [] #List of possible words
        self.RandomWord = "" #Word chosen
        self.letters = [] #Letters in word
        self.print = "" #Printed message
        self.guessed_letters = [] #Letters already guessed
        self.hp = 5 #Health of parachuter
        self.word_complete = False #Boolean to see if word is complete
        with open("game/wordlist.txt",'r') as f: #Accesses the text file and adds each word to a list
            for line in f:
                for word in line.split():
                    self.words.append(word)
        
    def choose_word(self): #A word is chosen from the list at random as well as seperates each letter of said word into a list of individual letters
        self.RandomWord = random.choice(self.words)
        for x in range(len(self.RandomWord)):
            self.letters.append(self.RandomWord[x])
    
    def create_print(self): #Creates the blanks and letters above the parachuters
        self.print = ""
        for x in self.letters: #For each letter of the word, it adds a blank space if the letter hasn't been guessed yet and the letter itself if it has been
            if x in self.guessed_letters:
                self.print += f" {x.upper()} "
            else:
                self.print += f" _ "
    
    def check_word(self): #This checks the word to see if it is completly guessed or not by assuming the word is completed until it finds a letter that hasn't been guessed yet. If it is able to go through each letter without finding a letter that isn't in the word, then the word is complete.
        for y in self.letters:
            if y in self.guessed_letters:
                self.word_complete = True
            else:
                self.word_complete = False
                break
