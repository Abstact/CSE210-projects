from game.casting.actor import Actor
from game.casting.actor2 import Actor2


class Score(Actor, Actor2):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, position, player):
        super().__init__()
        self._name = player
        self._points = 0
        self.add_points(0)
        self.set_position(position)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")

    def get_name(self):
        """Return the name of the Player
        """
        return self._name

    def get_points(self):
        """Return points of the Player
        """
        return self._points
