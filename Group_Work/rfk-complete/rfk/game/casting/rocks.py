import random
from game.casting.actor import Actor;
from game.shared.color import Color;
from game.shared.point import Point;

class Rock(Actor):
    """
        This is a Rock for the game.
        A class that inherits from Actor.
    """

    def __init__(self):
        super().__init__()

        # Rock appearance
        super().set_text("O")

        super().set_points(-1) #removes a point for every rock hit

        speed = random.randrange(1,15) # set the velocity
        super().set_velocity(Point(0,speed))

        red = random.randrange(150,200)
        green = random.randrange(50, 75) 
        color = Color(red, green, green) # random dark red color
        super().set_color(color)