from typing import Self

from ..utility.position     import Vector2D, Direction
from ..utility.command_enum import Command

class Car:
    """Car for simulation.

    Attributes:
        name: (str) Name of car.
        initial_position: (Vector2D) Initial position of car in (x, y).
        position: (Vector2D) Current position of car in (x, y).
        initial_direction: (Direction) Initial forward direction of car.
        direction: (Direction) Current forward direction of car.
        commands: (list[Command]) Simulation commands of car.
    """

    def __init__(self, name: str, position: Vector2D, direction: Direction, commands: list[Command]):
        """Initialization

        Arguments:
            name: (str) Name of car.
            position: (Vector2D) Position of car in (x, y).
            direction: (Direction) Forward direction of car.
            commands: (list[Command]) Simulation commands of car.
        """
        self.name              = name

        # Position.
        self.initial_position  = position
        self.position          = position

        # Forward facing direction.
        self.initial_direction = direction
        self.direction         = direction

        # Commands list.
        self.commands          = commands

        # Collision information.
        self.collided_cars     = []   # List of collided cars.
        self.collided_step     = None # Collision at step.

    def get_new_forward_position(self) -> Vector2D:
        """Gets a new forward position in (x, y) by car's current position
        and forward direction.
        
        Returns:
            Vector2D: The new forward position.
        """
        return self.position + self.direction
    
    def rotate_left(self):
        """Rotate forward direction of car to the left."""
        self.direction = Direction.rotate_left(self.direction)
    
    def rotate_right(self):
        """Rotate forward direction of car to the left."""
        self.direction = Direction.rotate_right(self.direction)

    def get_initial_status(self) -> str:
        """Get car initial status in string.
        
        Returns:
            str: Initial status of the car's name, position, direction and commands.
        """
        return f"{self.name}, {self.initial_position} {self.initial_direction.name}, {Command.commands_to_string(self.commands)}"
    
    def get_current_status(self) -> str:
        """Get car current status in string.
        
        Returns:
            str: Current status of the car's name, position, direction and if it 
            has collided with other cars.
        """
        if self.collided_cars:
            return f"{self.name}, collides with {','.join(sorted(c.name for c in self.collided_cars))} at {self.position} at step {self.collided_step}"
        else:
            return f"{self.name}, {self.position} {self.direction.name}"
        
    def has_collided(self) -> bool:
        """Checks if car has collided.
        
        Returns:
            bool: True if collided with other cars, otherwise False.
        """
        return len(self.collided_cars) > 0

    def set_collision(self, collided_cars: list[Self], collided_step: int):
        """Set collide information of car.

        Arguments:
            collided_cars: (list[Car]) Cars collided with this car.
            collided_step: (int) Step of the collision.
        """
        self.collided_cars = collided_cars
        self.collided_step = collided_step