from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__() 
        super().set_text("*") #this is what the artifact will look like

        super().set_points(+1) #this adds a point for each artifact hit
        
