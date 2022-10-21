"""
holds secret word
letters guessed
printing of image for game

"""
import random

with open("wordlist.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
  
    # print random string
    print(random.choice(words))
#class parachuter:


#       ___
#      /   \
#       ---
#       \  /
#        \/
#         0
#       / | \
#        / \
#
#     ^^^^^^^^^

    