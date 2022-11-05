import random

from game.casting.rocks import Rock
from game.casting.artifact import Artifact

from game.shared.point import Point


MAX_ARTIFACTS = 15
MAX_ROCKS = 20

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        velocity._y = 0 #constrains the velocity to x axis only
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        rocks = cast.get_actors("rocks")

        cell_size = self._video_service.get_cell_size()

        banner.set_text(f"Score: {self._get_score()}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        if len(rocks) < MAX_ROCKS:
            if random.randrange(0,10) == 8:
                new_rock = Rock()

                column = int(max_x / cell_size)
                location = Point(random.randrange(column) * cell_size, 0)
                new_rock.set_position(location)
                cast.add_actor("rocks", new_rock)

        for rock in rocks:
            rock.move_next(max_x, max_y)
            y = rock.get_position().get_y()

            if robot.get_position().equals(rock.get_position()):
                self._add_score(rocks.get_points())
                cast.remove_actor("rocks", rock)
            elif y > max_y - cell_size:
                cast.remove_actor("rocks", rock)

        if len(artifacts) < MAX_ARTIFACTS:
            if random.randrange(0,10) == 8:
                new_artifact = Artifact()

                column = int(max_x / cell_size)
                location = Point(random.randrange(column) * cell_size, 0)
                new_artifact.set_position(location)
                cast.add_actor("rocks", new_artifact)

        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
            y = artifact.get_position().get_y()

            if robot.get_position().equals(artifact.get_position()):
                self._add_score(artifacts.get_points())
                cast.remove_actor("artifact", artifact)
            elif y > max_y - cell_size:
                cast.remove_actor("artifacts", artifact)
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()

    def _add_score(self, points):
        """
            Adds the earned points to the score
            Args:
                points: points to add
        """
        self._score += points
    
    def _get_score(self):
        """
            Returns the current score 
        """
        return self._score