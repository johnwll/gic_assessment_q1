from pathlib import Path
import sys, subprocess

CONST_PROJNAME    = "car_simulator_project"
CONST_WIN32       = "win32"
cwd               = Path.cwd()
project_directory = cwd / CONST_PROJNAME

# Install requirements.
subprocess.run(['pip', 'install', '-r', 'requirements.txt'], cwd=project_directory)

# Clear console.
subprocess.run("cls" if sys.platform == CONST_WIN32 else "clear", shell=True)

# Run simulator.
try:
    subprocess.run(['py', '-m', CONST_PROJNAME], cwd=cwd)
except KeyboardInterrupt:
    pass