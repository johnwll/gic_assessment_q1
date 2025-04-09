import logging
from pathlib import Path

from .config                   import CONFIG_LOGFILENAME, CONFIG_LOGNAME
from .result                   import Result
from .input_parser             import InputParser
from ..car_simulator.simulator import CarSimulator
from ..utility.utility         import get_root_package

class CarSimulatorController:
    """Controller for the car simulator.

    Parses and validates user inputs used by the car simulator.
    Reusable by other user interface layer.

    Attributes:
        simulator: (CarSimulator) The car simulator.
    """

    def __init__(self):
        """Initialization"""
        self.__setup_logging()
        self.simulator = CarSimulator(self.logger)

    def set_field_dimension(self, user_input: str) -> Result:
        """Set dimension of the car field.
        
        Arguments:
            user_input: (str) Dimension of field. [width height]

        Returns:
            Result: (Ok, Dimension) if dimension of field is set.
        """
        result = InputParser.parse_field_dimension(user_input)
        if not result.ok():
            return result

        dimension = result.object
        return self.simulator.set_world_dimension(dimension)

    def add_car(self, name: str, position_direction: str, commands: str) -> Result:
        """Add car to the field.
        
        Arguments:
            name: (str) Name of car.
            position_direction: (str) Position and direction. [x y Direction]
            commands: (str) Car commands.

        Returns:
            Result: (Ok, Car) if car added to field.
        """
        result = InputParser.parse_car(name, position_direction, commands, self.simulator)
        if not result.ok():
            return result
        
        car = result.object
        return self.simulator.add_car(car)
    
    def validate_car_name(self, user_input: str) -> Result:
        """Validates car name.
        
        Arguments:
            user_input: (str) Name of car.

        Returns:
            Result: (Ok, Name) if car name is valid.
        """
        return InputParser.parse_car_name(user_input, self.simulator)
    
    def validate_car_position_direction(self, user_input: str) -> Result:
        """Validates car position and direction.
        
        Arguments:
            user_input: (str) Position and direction. [x y Direction]

        Returns:
            Result: (Ok, (Position, Direction))) if car position and direction is valid.
        """
        return InputParser.parse_car_position_direction(user_input, self.simulator)
    
    def validate_car_commands(self, user_input: str) -> Result:
        """Validates car commands.
        
        Arguments:
            user_input: (str) Car commands.

        Returns:
            Result: (Ok, list[Command]) if car commands are valid.
        """
        return InputParser.parse_car_commands(user_input)

    def get_car_list(self) -> list[str]:
        """Return initial status of all cars in list of string.

        Returns:
            list[str]: List of string of initial status of all cars.
        """
        return self.simulator.get_cars_status()
    
    def get_simulation_result(self) -> list[str]:
        """Return current status of all cars in list of string.
        
        Returns:
            list[str]: List of string of current simulation status of all cars.
        """
        return self.simulator.get_simulation_result()

    def run_simulation(self):
        """Runs the simulation for the car simulator."""
        self.simulator.simulate()

    def reinitialize_simulator(self):
        """Reinitialize the car simulator."""
        self.simulator.initialize()
    
    def __setup_logging(self):
        """Sets up logging."""
        log_filename = Path.cwd() / get_root_package() / CONFIG_LOGFILENAME
        logging.basicConfig(filename = log_filename, 
                            level    = logging.DEBUG,
                            format   = "%(levelname)s:%(filename)s:%(lineno)s - %(funcName)20s(): %(message)s")
        self.logger = logging.getLogger(CONFIG_LOGNAME)