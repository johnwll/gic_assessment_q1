# GIC Test Q1 - Car Simulator

Purpose of this car simulator program is to simulate simple car movements based on user inputs.

## Index

- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Usage](#usage)
- [Unit Test](#unit-test)

## Project Structure

The root package is named "car_simulator_project".

The sub-packages and description:


| Package                  | Description                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------- |
| car_simulator            | Car simulator logic.                                                                         |
| car_simulator_controller | Controller interface that can be used to access the car simulator logic.                     |
| car_simulator_interface  | Console user interface for users to interact with the car simulator.                         |
| unit_test                | Unit tests for pytest.                                                                       |
| utility                  | Utility package containing utility classes and functions that can be shared across packages. |

## Requirements

Python version 3.13.2

To install python requirements:

```sh
cd car_simulator_project
pip install -r requirements.txt
```

## Usage

To run the car simulator:

```sh
py run_simulator.py
```

## Unit Test

Unit testing is done with pytest.
To run test script:

```sh
py run_tests.py
```
