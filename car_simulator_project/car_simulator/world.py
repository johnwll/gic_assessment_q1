from collections import defaultdict

from .consts            import CONST_MINWIDTH, CONST_MINHEIGHT
from .car               import Car
from ..utility.position import Vector2D

class World:
    """World of the simulation. Containing all the cars.

    Attributes:
        cars: (list[Car]) List of all cars in the world.
        position_map: (defaultdict{Vector2D->set}) Map from position to a set of cars. 
        Mainly used for car collision checking.
        dimension: (Vector2D) Width and height of the world field.
    """

    def __init__(self):
        """Initialization"""
        self.cars         = []
        self.position_map = defaultdict(set)
        self.dimension    = Vector2D(CONST_MINWIDTH, CONST_MINHEIGHT)

    def add_car(self, car: Car):
        """Add a car to the world."""
        self.cars.append(car)
        self.add_car_to_map(car)

    def move_car(self, car: Car, new_position: Vector2D):
        """Move car in world.

        Arguments:
            car: (Car) Car to be moved.
            new_position: (Vector2D) New position of the car.
        """
        self.remove_car_from_map(car)
        car.position = new_position
        self.add_car_to_map(car)

    # Checks #

    def has_car_with_name(self, name: str) -> bool:
        """Check car with name exists in the world.

        Arguments:
            name: (str) Name of car to check.
        
        Returns:
            bool: True if any car with name in world, otherwise False.
        """
        return any(car for car in self.cars if car.name == name)

    def has_car_at_position(self, position: Vector2D) -> bool:
        """Check any car in position exists in the world.

        Arguments:
            position: (Vector2D) Position to check.
        
        Returns:
            bool: True if any car in position of world, otherwise False.
        """
        return position in self.position_map
    
    def out_of_bounds(self, position: Vector2D) -> bool:
        """Check if position is out of world boundary.

        Arguments:
            position: (Vector2D) Position to check.
        
        Returns:
            bool: True if out of world boundary, otherwise False.
        """
        return (position.x < 0 or position.x >= self.dimension.x) or \
               (position.y < 0 or position.y >= self.dimension.y)
    
    def is_car_collided(self, car: Car) -> bool:
        """Check if the car has collided.

        Arguments:
            car: (Car) Car to check for collision status.
        
        Returns:
            bool: True if car has collided with another car, otherwise False.
        """
        return len(self.position_map[car.position]) >= 2
    
    def get_collided_cars(self, car: Car) -> list[Car]:
        """Get all the cars collided with the current car.
        
        Arguments:
            car: (Car) Current car to get all other collided cars of.
        
        Returns:
            list[Car]: List of cars that are collided with the current car.
        """
        collided_cars = list(self.position_map[car.position])
        collided_cars.remove(car)
        
        return collided_cars

    def add_car_to_map(self, car: Car):
        """Add car into the car set of the position map.
        
        Arguments:
            car: (Car) Current car to be added.
        """
        self.position_map[car.position].add(car)

    def remove_car_from_map(self, car: Car):
        """Remove car from the car set of the position map.
        
        Arguments:
            car: (Car) Current car to be removed.
        """
        self.position_map[car.position].remove(car)