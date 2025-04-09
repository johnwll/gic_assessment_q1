from enum   import Enum
from typing import Self

class Command(Enum):
    """Car Commands."""

    L: str = "Rotate Left"
    R: str = "Rotate Right"
    F: str = "Move Forward"

    @staticmethod
    def commands_to_string(commands: list[Self]) -> str:
        """Converts commands to string.
        
        Returns:
            str: String of car commands.
        """
        return "".join(command.name for command in commands)
    
    @staticmethod
    def string_to_commands(commands: str) -> list[Self]:
        """Converts string to commands.
        
        Returns:
            list[Command]: List of car commands.
        """
        return [Command[command] for command in commands]