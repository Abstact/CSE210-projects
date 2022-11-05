import random
from game.casting.actor import Actor;
from game.shared.color import Color;
from game.shared.point import Point;

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
        
        speed = random.randrange(1,15) # set the velocity
        super().set_velocity(Point(0,speed))

        red = random.randrange(20,100)
        green = random.randrange(50, 75) 
        color = Color(red, green, green) # random dark red color
        super().set_color(color)