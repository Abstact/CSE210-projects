"""
user.py

A code that interprets input

main():
    The user is asked to input his/her/their guess.

"""

class User:
    def get_input(self):
        """
            Gets the letter guessed by the user. Also makes 
            sure that the user input is only one letter.
        """

        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
                    'y', 'z'] # The list of the letters of the English Alphabet

        try:
            letter = input("\nPlease guess a letter: ") # Gets the user's guess

            # Check whether the input is a single letter
            while letter.lower() not in alphabet: # Check if letter is in the alphabet list
                letter = input("\nPlease input a single letter: ") # Ask for another input if not a single letter
            else:
                print(f"\nYour guess is: {letter.upper()}") # Prints out the user's guess
                return letter.lower() # Returns the letter guessed to be used in the director file

        except TypeError or Exception as err:
            print(f"Error found: {err}") # Prints the error if found