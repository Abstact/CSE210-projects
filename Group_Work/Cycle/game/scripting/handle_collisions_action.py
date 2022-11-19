import constants
import time
from game.casting.actor import Actor
from game.casting.actor2 import Actor2
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            # self._handle_food_collision(cast)      # We don't need this 
            self._handle_tail_growth(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
            
    def _handle_tail_growth(self, cast):
        # player1 = cast.get_first_actor("snakes")
        # player2 = cast.get_first_actor("boa")

        # tail_grow_count = 1

        # player1.grow_tail(tail_grow_count)
        # player2.grow_tail(tail_grow_count)

    # def _handle_food_collision(self, cast):        # We don't need this
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        score2 = cast.get_first_actor("scores")

        food = cast.get_first_actor("foods")     
        
        snake = cast.get_first_actor("snakes")
        boa = cast.get_first_actor("boa")

        head = snake.get_head()
        head2 = boa.get_head()

        if head.get_position().equals(food.get_position()):
            points = food.get_points()
            snake.grow_tail(points)
            score.add_points(points)
            food.reset()
        elif head2.get_position().equals(food.get_position()):
            points = food.get_points()
            snake.grow_tail(points)
            score2.add_points(points)
            food.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycles collides with one of its trails.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        #cycle 1
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]

        #cycle 2
        boa = cast.get_second_actor("boa")
        head2 = boa.get_segments()[0]
        segments2 = boa.get_segments()[1:]
        scores = cast.get_actors('scores')


        #cycle 1 collision
        for segment in segments2:
            if head.get_position().equals(segment.get_position()) or head.get_position().equals(head2.get_position()):
                scores[1].add_points(1)
                self._is_game_over = True
                
        # cycle 2 collision
        for segment in segments:
            if head2.get_position().equals(segment.get_position()) or head2.get_position().equals(head.get_position()):
                scores[0].add_points(1)
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle and trail white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        boa = cast.get_first_actor("boa")
        scores = cast.get_actors("scores")

        if self._is_game_over:
            segments = snake.get_segments()
            seg2 = boa.get_segments()

            # food = cast.get_first_actor("foods")   # We don't need this

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(f"Game Over! {scores[0].get_name() if scores[0].get_points() > 0 else scores[1].get_name()} won")
            message.set_position(position)
            cast.add_actor("messages", message)

            # food.set_color(constants.WHITE)      # We don't need this

            for segment in segments:
                segment.set_color(constants.WHITE)
            for segment in seg2:
                segment.set_color(constants.WHITE)