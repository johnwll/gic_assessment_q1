from enum import Enum

class UserOption1(Enum):
    """User options for adding car and running simulation."""
    ADD_CAR: str = "Add a car to field"
    RUN_SIM: str = "Run simulation"

class UserOption2(Enum):
    """User options after running simulation"""
    START_OVER: str = "Start over"
    EXIT      : str = "Exit"