import sys

from .car_simulator_interface.interface import CarSimulatorInterface

def main():
    """Main execution."""
    interface = CarSimulatorInterface()
    interface.display()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program exited.")
        sys.exit(0)