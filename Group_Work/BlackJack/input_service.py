class Input():
    
    def __init__(self) -> None:
        self.keep_playing = True

    def keep_playing(self):
        """
            Asks the player if they want to continue the game
        """
        def ask():

            ask_continue = input("Do you want to continue(Y/N)?\n\t→ ")

            if ask_continue.upper() == "Y":
                self.keep_playing = True
                
            elif ask_continue.upper() == "N":
                self.keep_playing = False

            else:                                   # Prevents error from user not typing y or n
                print("Please enter Y or N")
                ask()

        ask()
    
    def hit_stand(self):
        """
            Asks the player if they want to hit ot stand
        """

        ask_continue = input("Do you want to hit ot stand (H/S)?\n\t→ ")

        if ask_continue.upper() == "H":
            self.keep_playing = True
            
        elif ask_continue.upper() == "S":
            self.keep_playing = False