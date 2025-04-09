from .car                              import Car
from .world                            import World
from ..car_simulator_controller.result import Result
from ..utility.position                import Vector2D
from ..utility.command_enum            import Command

class CarSimulator:
    """The car simulator.

    Attributes:
        world: (World) A container for all the cars.
        simulating_cars: (list[Car]) A list of currently simulating cars.
    """
    
    def __init__(self, logger):
        """Initialization.

        Arguments:
            logger: Logger for debug information etc.
        """
        self.logger = logger
        self.initialize()

    def initialize(self):
        """Initialize simulator. Can be used for re-initialization."""
        self.world           = World()
        self.simulating_cars = []

    def add_car(self, car: Car) -> Result:
        """Add car to the simulator after validation.
        
        Arguments:
            car: (Car) Car to be added.

        Return:
            Result: (Ok, Car) if validation passed and car added to world.
        """
        result = self.validate_car_name(car.name)
        if not result.ok():
            return result
        
        result = self.validate_car_position(car.position)
        if not result.ok():
            return result

        self.world.add_car(car)
        self.logger.debug(f"Car added: {car.get_initial_status()}")

        return Result(True, object = car)
        
    def set_world_dimension(self, dimension: Vector2D) -> Result:
        """Set width and height of the world.

        Arguments:
            dimension: (Vector2D) Width and height of the world.

        Return:
            Result: (Ok, Dimension set) if validation passed and world dimension set.
        """
        result = self.validate_world_dimension(dimension)
        if not result.ok():
            return result
        
        self.world.dimension = dimension

        return Result(True, object = dimension)

    def simulate(self):
        """Run simulation for all the cars.

        The max number of steps simulated is always lesser or equals to the longest car command.
        Runs simulation until either max number of steps reached or no more cars available for simulation.

        For every simulation step, update the current simulating cars and then simulate the current step.

        Time Complexity: O(p*n^2), p is length of longest command, n is number of cars.
        """
        self.simulating_cars = self.world.cars
        max_steps = max((len(car.commands) for car in self.simulating_cars), default=0)

        self.logger.debug(f"Simulate World: ({self.world.dimension.x} x {self.world.dimension.y}), Total Cars: {len(self.world.cars)}")

        for step in range(max_steps):
            self.update_simulation_cars(step)

            if not self.simulating_cars:
                break

            self.simulate_step(step)

    def update_simulation_cars(self, step: int):
        """Update the next list of cars for simulation.

        For every car, if it is currently collided update its collision information;
        else if there are still remaining commands add it to the next list of cars
        for simulation.

        Arguments:
            step: (int) Current simulating step.
        """
        next_cars = []

        for car in self.simulating_cars:
            if self.world.is_car_collided(car):
                self.update_collision(car, step)
            else:
                if step < len(car.commands):
                    # If car still has next simulation step, add to next list of cars.
                    next_cars.append(car)

        self.simulating_cars = next_cars
    
    def update_collision(self, car: Car, step: int):
        """Update the collision information of the current car and other collided cars.

        Arguments:
            car: (Car) Current car to update collision.
            step: (int) Current simulating step.
        """
        # Update current car collision information.
        car.set_collision(self.world.get_collided_cars(car), step)

        # Update other cars that are not collided to be collided.
        for other in car.collided_cars:
            if not other.has_collided():
                other.set_collision(self.world.get_collided_cars(other), step)

    def simulate_step(self, step: int):
        """Simulate the current step.

        For every car, simulate for the current step based on the car's current command.
        
        Arguments:
            step: (int) Current simulating step.
        """
        self.logger.debug(f"Executing Step: {step}")

        for car in self.simulating_cars:
            command = car.commands[step]

            old_position, old_direction = car.position, car.direction
            match command:
                case Command.L:
                    car.rotate_left()
                    self.logger.debug(f"\tCar {car.name}: {command.value} from {old_direction.value} to {car.direction.value}. [Success]")
                case Command.R:
                    car.rotate_right()
                    self.logger.debug(f"\tCar {car.name}: {command.value} from {old_direction.value} to {car.direction.value}. [Success]")
                case Command.F:
                    new_position = car.get_new_forward_position()
                    if not self.world.out_of_bounds(new_position):
                        self.world.move_car(car, new_position)
                        self.logger.debug(f"\tCar {car.name}: {command.value} {car.direction.value} from {old_position} to {new_position}. [Success]")
                    else:
                        self.logger.debug(f"\tCar {car.name}: {command.value} {car.direction.value} from {old_position} to {new_position}. [Failed]")
    
    def get_cars_status(self) -> list[str]:
        """Return initial status of all cars.
        
        Returns:
            list[str]: List of string of initial status of all cars.
        """
        return [f"- {car.get_initial_status()}" for car in self.world.cars]
    
    def get_simulation_result(self) -> list[str]:
        """Return current status of all cars.
        
        Returns:
            list[str]: List of string of current simulation status of all cars.
        """
        return [f"- {car.get_current_status()}" for car in self.world.cars]

    # Validation #

    def validate_world_dimension(self, dimension: Vector2D) -> Result:
        """Validates the world dimension before setting.

        Arguments:
            dimension: (Vector2D) New dimension of the world.

        Returns:
            Result: (Ok, Dimension) if dimension is valid.
        """
        if dimension.x <= 0:
            return Result(False, f"Width must be greater than zero.")
        
        if dimension.y <= 0:
            return Result(False, f"Height must be greater than zero.")
        
        return Result(True, object = dimension)
    
    def validate_car_name(self, name: str) -> Result:
        """Validates name of the car if already exists in world.

        Arguments:
            name: (str) Name of the car.

        Returns:
            Result: (Ok, Name) if car name is valid.
        """
        if self.world.has_car_with_name(name):
            return Result(False, f"Car with name {name} already exists.")
        
        return Result(True, object = name)
    
    def validate_car_position(self, position: Vector2D) -> Result:
        """Validates car positioning in world.

        Arguments:
            position: (Vector2D) Position of car.

        Returns:
            Result: (Ok, Position) if position is valid.
        """
        if self.world.has_car_at_position(position):
            return Result(False, f"Another car is already in position {position}.")
        
        if self.world.out_of_bounds(position):
            return Result(False, f"Position {position} is out of the field bounds.")
        
        return Result(True, object = position)