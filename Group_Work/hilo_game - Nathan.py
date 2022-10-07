import random

def main():
    print("Welcome to Hi-Lo!")
    director = Director()
    director.play_game()

class Director:
    def __init__(self):
        self.playing = True
        self.previous_card = Card()
        self.next_card = Card()
        self.you = Player()

    def play_game(self):
        self.previous_card.draw_card()
        while self.playing:
            self.hi_lo()
            self.cleanup()
    
    def hi_lo(self):
        if not self.playing:
            return

        while True:
            self.next_card.draw_card()
            if self.previous_card.value == self.next_card.value:
                continue
            else:
                break

        print(f"The card is: {str(self.previous_card.value)}")

        while True:
            h_or_l = input("Higher or Lower? [h/l] ")

            if h_or_l.lower() == "l" or h_or_l.lower() == "h":
                self.you.guess_high = (h_or_l.lower() == "h")
                break
            else:
                print("Please enter either h or l")
                continue

        print(f"Next card is: {str(self.next_card.value)}")

        self.compare()
        
        print(f"Your score: {str(self.you.points)}")
        print()

    def cleanup(self):
        if not self.playing:
            return
        
        if self.you.points <= 0:
            print("GAME OVER")

        while True:
            play_again = input("Play Again? [y/n]")
            print()
            if play_again.lower() == "y":
                self.previous_card.value = self.next_card.value
                self.playing = True
                return
            elif play_again.lower() == "n":
                self.playing = False
                return
    
    def compare(self):
        card1 = self.previous_card.value
        card2 = self.next_card.value

        if card1 > card2:
            if self.you.guess_high:
                self.you.wrong()
                print("Too Bad!")
            else:
                self.you.right()
                print("Great Guess")
        else:
            if self.you.guess_high:
                self.you.right()
                print("Great Guess")
            else:
                self.you.wrong()
                print("Too Bad!")
        

class Card:
    def __init__(self):
        self.value = 0
    def draw_card(self):
        self.value = random.randrange(1,14)

class Player:
    def __init__(self):
        self.points = 300
        self.guess_high = True
    def wrong(self):
        self.points -= 75
    def right(self):
        self.points += 100

if __name__ == "__main__":
    main()