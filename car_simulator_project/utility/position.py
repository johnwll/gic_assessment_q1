from enum import Enum
from typing import Self

class Vector2D:
    """2D Point.
    
    Attributes:
        x: (int) x-axis value.
        y: (int) y-axis value.
    """

    def __init__(self, x: int = 0, y: int = 0):
        """Initialization.
        
        Arguments:
            x: (int) x-axis value.
            y: (int) y-axis value.
        """
        self.x = x
        self.y = y

    def __eq__(self, other: Self) -> bool:
        """Equality check.
        
        Returns:
            bool: True if x and y are the same value, otherwise False.
        """
        return self.x == other.x and self.y == other.y

    def __add__(self, other) -> Self:
        """Addition operator.
        
        Arguments:
            other: Other data type.

        Returns:
            Vector2D: Vector2D added with other data type.
        """
        # Add Direction.
        if other in Direction:
            vector = Direction.to_vector(other)
            return Vector2D(self.x + vector.x, self.y + vector.y)
        
        return Vector2D(self.x, self.y)
    
    def __hash__(self):
        """Hash function.
        
        Returns:
            Hash value.
        """
        return hash((self.x, self.y))
    
    def __repr__(self):
        """Debug purposes.
        
        Returns:
            str: (x,y) value.
        """
        return f"({self.x},{self.y})"

class Direction(Enum):
    """Direction."""

    N: str = "North"
    E: str = "East"
    S: str = "South"
    W: str = "West"

    @staticmethod
    def to_vector(direction: Self) -> Vector2D:
        """Convert to Vector2D.
        
        Returns:
            Vector2D: Vector2D of the Direction.
        """
        match direction:
            case Direction.N:
                return Vector2D(0, 1)
            case Direction.E:
                return Vector2D(1, 0)
            case Direction.S:
                return Vector2D(0, -1)
            case Direction.W:
                return Vector2D(-1, 0)
            case _:
                return Vector2D(0, 0)
            
    @staticmethod
    def rotate_left(direction: Self) -> Self:
        """Rotate direction to the left.

        Arguments:
            direction: (Direction) Direction to left rotate.
        
        Returns:
            Direction: Left rotated direction.
        """
        directions = list(Direction)
        return directions[(directions.index(direction) - 1) % len(directions)]
            
    @staticmethod
    def rotate_right(direction: Self) -> Self:
        """Rotate direction to the right.

        Arguments:
            direction: (Direction) Direction to right rotate.
        
        Returns:
            Direction: Right rotated direction.
        """
        directions = list(Direction)
        return directions[(directions.index(direction) + 1) % len(directions)]
    
    @staticmethod
    def string_to_direction(direction: str) -> Self:
        """Converts string to Direction.

        Arguments:
            direction: (str) Direction in string value.
        
        Returns:
            Direction: Direction enum of the string value.
        """
        return Direction[direction]