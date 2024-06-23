import subprocess
import os
from pathlib import Path

current_dir = Path(__file__).parent.absolute()
venv_dir = current_dir
os.chdir(venv_dir)
subprocess.run(['311_venv/Scripts/python.exe', 'install_package.py'])
subprocess.run(['311_venv/Scripts/python.exe', 'main.py'])