from enum import Enum

from .options_enum                         import UserOption1, UserOption2
from ..car_simulator_controller.controller import CarSimulatorController
from ..car_simulator_controller.result     import Result

class CarSimulatorInterface:
    """User interface of the car simulator.
        
        Attributes:
            controller: (CarSimulatorController) Controller of car simulator.
    """

    def __init__(self):
        """Initialization."""
        self.controller = CarSimulatorController()

    def display(self):
        """Display user interface in console."""
        while 1:
            self.display_welcome_message()

            # Field dimension.
            self.prompt_field_dimension()

            # Add cars or Run simulation.
            while 1:
                option = self.prompt_options(UserOption1)
                match option:
                    case UserOption1.ADD_CAR:
                        self.prompt_add_car()
                        self.display_car_list()
                        continue
                    case UserOption1.RUN_SIM:
                        self.controller.run_simulation()
                        self.display_simulation_result()
                        break
            
            # Start over or Exit.
            option = self.prompt_options(UserOption2)
            match option:
                case UserOption2.START_OVER:
                    self.controller.reinitialize_simulator()
                    continue
                case UserOption2.EXIT:
                    self.display_exit_message()
                    break

    # Prompt #

    def prompt_field_dimension(self) -> str:
        """Prompt field dimension from user.

        Returns:
            str: Field dimension from user if valid.
        """
        message = "Please enter the width and height of the simulation field in x y format:\n"
        while 1:
            while not (user_input := input(message).strip()):
                pass

            result = self.validate_field_dimension(user_input)
            if not result.ok():
                self.display_error(result.error)
                continue
            
            # Set field dimension
            result = self.controller.set_field_dimension(user_input)
            if not result.ok():
                self.display_error(result.error)
                continue
            
            self.display_message(f"You have created a field of {result.object.x} x {result.object.y}.\n")

            return user_input
    
    def prompt_car_name(self) -> str:
        """Prompt car name from user.

        Returns:
            str: Car name from user if valid.
        """
        message = "Please enter the name of the car:\n"
        while 1:
            while not (user_input := input(message).strip()):
                pass

            result = self.controller.validate_car_name(user_input)
            if not result.ok():
                self.display_error(result.error)
                continue
            
            return user_input

    def prompt_car_position_direction(self, name: str) -> str:
        """Prompt car position and direction from user.

        Arguments:
            name: (str) Car name.

        Returns:
            str: Position and direction from user if valid.
        """
        message = f"Please enter initial position of car {name} in x y Direction format:\n"
        while 1:
            while not (user_input := input(message).strip()):
                pass
            
            result = self.validate_car_position_direction(user_input)
            if not result.ok():
                self.display_error(result.error)
                continue
            
            result = self.controller.validate_car_position_direction(user_input)
            if not result.ok():
                self.display_error(result.error)
                continue

            return user_input

    def prompt_car_commands(self, name: str) -> str:
        """Prompt car commands from user.

        Arguments:
            name: (str) Car name.

        Returns:
            str: Commands from user if valid.
        """
        message = f"Please enter the commands for car {name}:\n"
        while 1:
            while not (user_input := input(message).strip()):
                pass
            
            result = self.controller.validate_car_commands(user_input)
            if not result.ok():
                self.display_error(result.error)
                continue

            return user_input

    def prompt_add_car(self):
        """Prompt to add car."""
        while 1:
            name               = self.prompt_car_name()
            position_direction = self.prompt_car_position_direction(name) 
            commands           = self.prompt_car_commands(name)

            # Add car if all prompts succeeded.
            result = self.controller.add_car(name, position_direction, commands)
            if not result.ok():
                self.display_error(result.error)
                continue

            break
    
    def prompt_options(self, options: Enum) -> Enum:
        """Prompt user options.

        Arguments:
            options: (Enum) Options in enum.

        Returns:
            Enum: Option enum selected by the user if valid.
        """
        option_list = [o for o in options]
        
        message = "Please choose from the following options:"
        for index, option in enumerate(option_list):
            message += f"\n[{index+1}] {option.value}"
        message += "\n"

        while 1:
            while not (user_input := input(message).strip()):
                pass
            
            result = self.validate_options(user_input, len(options))
            if not result.ok():
                self.display_error(result.error)
                continue

            selected_index  = result.object - 1
            selected_option = option_list[selected_index]
            return selected_option

    # Validation #

    def validate_field_dimension(self, user_input: str) -> Result:
        """Validates field dimension from user input.

        Arguments:
            user_input: (str) Dimension of field.

        Returns:
            Result: (Ok) if dimension is valid.
        """
        width_height = user_input.split(" ")

        if len(width_height) != 2:
            return Result(False, f"Invalid width and height of x y format ({user_input}).")
        
        return Result(True)
    
    def validate_car_position_direction(self, user_input: str) -> Result:
        """Validates car position and direction from user input.

        Arguments:
            user_input: (str) Car position and direction.

        Returns:
            Result: (Ok) if position and direction is valid.
        """
        position_direction = user_input.split(" ")
        
        if len(position_direction) != 3:
            return Result(False, f"Invalid car position of x y Direction format ({user_input}).")

        return Result(True)

    def validate_options(self, user_input: str, max_options: int) -> Result:
        """Validates options selected from user input.

        Arguments:
            user_input: (str) Option selected by user.
            max_options: (int) The maximum options allowed. (1-max_options)

        Returns:
            Result: (Ok, Option Enum) if option selected is valid.
        """
        message = f"Selected option must be number from 1 to {max_options}."

        try:
            option = int(user_input)
        except ValueError:
            return Result(False, message)
        
        if option <= 0 or option > max_options:
            return Result(False, message)
        
        return Result(True, object = option)
    
    # Display #

    def display_message(self, message: str):
        """Display message to console.

        Arguments:
            message: (str) Message to be displayed.
        """
        print(message)

    def display_error(self, error: str):
        """Display error message to console.

        Arguments:
            message: (str) Error message to be displayed.
        """
        print(error)

    def display_welcome_message(self):
        """Display welcome message to console."""
        self.display_message("Welcome to Auto Driving Car Simulation!\n")

    def display_exit_message(self):
        """Display exit message to console."""
        self.display_message("Thank you for running the simulation. Goodbye!")
        
    def display_car_list(self):
        """Display list of car status to console."""
        cars = self.controller.get_car_list()
        if cars:
            print("Your current list of cars are:")
            for car in cars:
                print(car)
        else:
            print("No cars available.")
        print()
    
    def display_simulation_result(self):
        """Display list of car current simulated status to console."""
        self.display_car_list()
        
        simulation_results = self.controller.get_simulation_result()
        if simulation_results:
            print("After simulation, the result is:")
            for result in simulation_results:
                print(result)
            print()