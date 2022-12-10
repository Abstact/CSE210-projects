class Input():
    
    def __init__(self) -> None:
        self.playing = True
        self.hit = True

    def keep_playing(self):
        """
            Asks the player if they want to continue the game
        """
        def ask():

            ask_continue = input("Do you want to continue(Y/N)?\n\t→ ")

            if ask_continue.upper() == "Y":
                self.playing = True
                
            elif ask_continue.upper() == "N":
                self.playing = False

            else:                                   # Prevents error from user not typing y or n
                print("Please enter Y or N")
                ask()
        ask()
    
    def hit_stand(self):
        """
            Asks the player if they want to hit ot stand
        """

        def ask_2():
            ask_continue = input("Do you want to hit or stand (H/S)?\n\t→ ")

            if ask_continue.upper() == "H":
                self.hit = True
                
            elif ask_continue.upper() == "S":
                self.hit = False
            
            else:
                print("Please enter H or S")
                ask_2()
        ask_2()