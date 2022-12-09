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

            else:
                print("Please enter Y or N")
                ask()

        ask()