import sys
from pathlib import Path

from .config                             import *
from ..car_simulator_interface.interface import CarSimulatorInterface

def interface_run():
    """Run the test interface."""
    CarSimulatorInterface().display()

def current_module_path():
    """Returns parent path of current module."""
    return Path(__file__).parent

def test_simulator_interface(capsys):
    """Test car simulator user interface.
    
    Arguments:
        capsys: Captures stdout from car simulator interface.
    """
    # Expected input and output test cases.
    directory_test_input  = current_module_path() / CONFIG_FOLDER_CASES_FOLDER / CONFIG_FOLDER_CASES_IN
    directory_test_output = current_module_path() / CONFIG_FOLDER_CASES_FOLDER / CONFIG_FOLDER_CASES_OUT

    sys_stdin = sys.stdin

    # For every input file assert expected output result.
    for test_input in directory_test_input.iterdir():
        test_output = directory_test_output / test_input.name
        if not test_output.is_file():
            continue

        with open(test_input, "r") as input_file:
            sys.stdin = input_file
            interface_run()
            stdout    = capsys.readouterr()
        
        with open(test_output, "r") as output_file:
            expected = output_file.read()

        assert stdout.out == expected, f"Test file input: {test_input.name}, output: {test_output.name} failed."

    sys.stdin = sys_stdin