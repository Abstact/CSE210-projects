"""
holds secret word
letters guessed
printing of image for game

"""
import random

class parachuter:


    words = []
    with open('wordlist.txt','r') as f:
        for line in f:
            for word in line.split():
                words.append(word)
    RandomWord = random.choice(words)

    print(RandomWord)

#     wordList = list(word)

#     wordAnswer = []
#     for i in range(len(word)):
# 	    wordAnswer.append('_')

<<<<<<< HEAD
#     guesses = 6
#     def printState(guesses):
# 	    myString = ""

# 	    if guesses == 1:
# 		    myString = "________      "
# 		    myString  = myString + '\n' + "|      ___      "
# 		    myString  = myString + '\n' + "|     /   \     "
# 		    myString  = myString + '\n' + "|      ---      "
# 		    myString  = myString + '\n' + "|      \  /     "
# 		    myString  = myString + '\n' + "|       \/      "
#           myString  = myString + '\n' + "|       0       "
#           myString  = myString + '\n' + "|     / | \     "
#           myString  = myString + '\n' + "|      / \      "
#           myString  = myString + '\n' + "|               "
#           myString  = myString + '\n' + "|   ^^^^^^^^^   "
#         elif guesses == 2:
#             myString  = "________      "
#             myString  = myString + '\n' + "|     /   \     "
#             myString  = myString + '\n' + "|      ---      "
#             myString  = myString + '\n' + "|      \  /     "
#             myString  = myString + '\n' + "|       \/      "
#             myString  = myString + '\n' + "|       0       "
#             myString  = myString + '\n' + "|     / | \     "
#             myString  = myString + '\n' + "|      / \      "
#             myString  = myString + '\n' + "|               "
#             myString  = myString + '\n' + "|   ^^^^^^^^^   "
#         elif guesses == 3:
#             myString  = "________      "
#             myString  = myString + '\n' + "|      ---      "
#             myString  = myString + '\n' + "|      \  /     "
#             myString  = myString + '\n' + "|       \/      "
#             myString  = myString + '\n' + "|       0       "
#             myString  = myString + '\n' + "|     / | \     "
#             myString  = myString + '\n' + "|      / \      "
#             myString  = myString + '\n' + "|               "
#             myString  = myString + '\n' + "|   ^^^^^^^^^   "
#         elif guesses == 4:
#             myString  = "________      "
#             myString  = myString + '\n' + "|      \  /     "
#             myString  = myString + '\n' + "|       \/      "
#             myString  = myString + '\n' + "|       0       "
#             myString  = myString + '\n' + "|     / | \     "
#             myString  = myString + '\n' + "|      / \      "
#             myString  = myString + '\n' + "|               "
#             myString  = myString + '\n' + "|   ^^^^^^^^^   "
#         elif guesses == 5:
#             myString = "________      "
#             myString  = myString + '\n' + "|       \/      "
#             myString  = myString + '\n' + "|       0       "
#             myString  = myString + '\n' + "|     / | \     "
#             myString  = myString + '\n' + "|      / \      "
#             myString  = myString + '\n' + "|               "
#             myString  = myString + '\n' + "|   ^^^^^^^^^   "
#         else:
#             myString = "________      "
#             myString  = myString + '\n' + "|       X       "
#             myString  = myString + '\n' + "|     / | \     "
#             myString  = myString + '\n' + "|      / \      "
#             myString  = myString + '\n' + "|               "
#             myString  = myString + '\n' + "|   ^^^^^^^^^   "
=======
    maxStates = 6
#keep on taking inputs while the either wins or hangman reaches state 7
    def printState(guesses):
        myString = ""

        if guesses == 1:
            myString = "________      "
            myString  = myString + '\n' + "|      ___      "
            myString  = myString + '\n' + "|     /   \     "
            myString  = myString + '\n' + "|      ---      "
            myString  = myString + '\n' + "|      \  /     "
            myString  = myString + '\n' + "|       \/      "
            myString  = myString + '\n' + "|       0       "
            myString  = myString + '\n' + "|     / | \     "
            myString  = myString + '\n' + "|      / \      "
            myString  = myString + '\n' + "|               "
            myString  = myString + '\n' + "|   ^^^^^^^^^   "
        elif guesses == 2:
            myString  = "________      "
            myString  = myString + '\n' + "|     /   \     "
            myString  = myString + '\n' + "|      ---      "
            myString  = myString + '\n' + "|      \  /     "
            myString  = myString + '\n' + "|       \/      "
            myString  = myString + '\n' + "|       0       "
            myString  = myString + '\n' + "|     / | \     "
            myString  = myString + '\n' + "|      / \      "
            myString  = myString + '\n' + "|               "
            myString  = myString + '\n' + "|   ^^^^^^^^^   "
        elif guesses == 3:
            myString  = "________      "
            myString  = myString + '\n' + "|      ---      "
            myString  = myString + '\n' + "|      \  /     "
            myString  = myString + '\n' + "|       \/      "
            myString  = myString + '\n' + "|       0       "
            myString  = myString + '\n' + "|     / | \     "
            myString  = myString + '\n' + "|      / \      "
            myString  = myString + '\n' + "|               "
            myString  = myString + '\n' + "|   ^^^^^^^^^   "
        elif guesses == 4:
            myString  = "________      "
            myString  = myString + '\n' + "|      \  /     "
            myString  = myString + '\n' + "|       \/      "
            myString  = myString + '\n' + "|       0       "
            myString  = myString + '\n' + "|     / | \     "
            myString  = myString + '\n' + "|      / \      "
            myString  = myString + '\n' + "|               "
            myString  = myString + '\n' + "|   ^^^^^^^^^   "
        elif guesses == 5:
            myString = "________      "
            myString  = myString + '\n' + "|       \/      "
            myString  = myString + '\n' + "|       0       "
            myString  = myString + '\n' + "|     / | \     "
            myString  = myString + '\n' + "|      / \      "
            myString  = myString + '\n' + "|               "
            myString  = myString + '\n' + "|   ^^^^^^^^^   "
        else:
            myString = "________      "
            myString  = myString + '\n' + "|       X       "
            myString  = myString + '\n' + "|     / | \     "
            myString  = myString + '\n' + "|      / \      "
            myString  = myString + '\n' + "|               "
            myString  = myString + '\n' + "|   ^^^^^^^^^   "
>>>>>>> 0785e91d52a09bfa8036abfb5682bceb9288d44a
