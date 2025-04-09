from .result                   import Result
from ..car_simulator.car       import Car
from ..car_simulator.simulator import CarSimulator
from ..utility.position        import Vector2D, Direction
from ..utility.command_enum    import Command

class InputParser:
    """Parses user input into data structure of car simulator."""

    @staticmethod
    def parse_field_dimension(user_input: str) -> Result:
        """Parse field dimension.

        Arguments:
            user_input: (str) Dimension of field.

        Returns:
            Result: (Ok, Dimension) if dimension is validated and parsed.
        """
        width, height = user_input.split(" ")

        try:
            width = int(width)
        except ValueError:
            return Result(False, f"Width must be an integer.")
        
        try:
            height = int(height)
        except ValueError:
            return Result(False, f"Height must be an integer.")
        
        dimension = Vector2D(width, height)
        return Result(True, object = dimension)
    
    @staticmethod
    def parse_car_name(user_input: str, simulator: CarSimulator) -> Result:
        """Parse car name.

        Arguments:
            user_input: (str) Position and direction. [x y Direction]
            simulator: (CarSimulator) Car simulator.

        Returns:
            Result: (Ok, Name) if car name validated.
        """
        return simulator.validate_car_name(user_input)
    
    @staticmethod
    def parse_car_position_direction(user_input: str, simulator: CarSimulator) -> Result:
        """Parse position and direction of car.

        Arguments:
            user_input: (str) Position and direction. [x y Direction]

        Returns:
            Result: (Ok, (Position, Direction)) if position and direction are validated and parsed.
        """
        x, y, direction = user_input.split(" ")

        try:
            x = int(x)
        except ValueError:
            return Result(False, f"X position must be an integer.")
        
        try:
            y = int(y)
        except ValueError:
            return Result(False, f"Y position must be an integer.")
        
        position = Vector2D(x, y)
        result   = simulator.validate_car_position(position)
        if not result.ok():
            return result
        
        # Direction
        try:
            direction_enum = Direction.string_to_direction(direction)
        except KeyError:
            valid_directions = [d.name for d in Direction]
            return Result(False, f"Direction '{direction}' is not valid. Valid directions are {valid_directions}.")

        return Result(True, object = (position, direction_enum))
    
    @staticmethod
    def parse_car_commands(user_input: str) -> Result:
        """Parse car commands.

        Arguments:
            user_input: (str) Car commands.

        Returns:
            Result: (Ok, list[Command]) if commands are validated and parsed.
        """
        # Commands
        for command in user_input:
            try:
                Command[command]
            except KeyError:
                valid_commands = [c.name for c in Command]
                return Result(False, f"Command '{command}' is not valid. Valid commands are {valid_commands}.")
            
        commands_list = Command.string_to_commands(user_input)

        return Result(True, object = commands_list)
    
    @staticmethod
    def parse_car(name: str, position_direction: str, commands: str, simulator: CarSimulator) -> Result:
        """Parse car.

        Arguments:
            name: (str) Name of car.
            position_direction: (str) Position and direction. [x y Direction]
            commands: (str) Car commands.

        Returns:
            Result: (Ok, Car) if car is validated and parsed.
        """
        result_name = InputParser.parse_car_name(name, simulator)
        if not result_name.ok():
            return result_name
        
        result_position = InputParser.parse_car_position_direction(position_direction, simulator)
        if not result_position.ok():
            return result_position
        
        result_commands = InputParser.parse_car_commands(commands)
        if not result_commands.ok():
            return result_commands
        
        name                = result_name.object
        position, direction = result_position.object
        commands            = result_commands.object
        
        car = Car(name, position, direction, commands)

        return Result(True, object = car)   
