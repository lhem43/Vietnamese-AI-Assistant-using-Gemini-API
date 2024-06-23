import subprocess

subprocess.run(['312_venv/Scripts/python.exe', '-m', 'pip', 'install', 'google.generativeai'])
subprocess.run(['311_venv/Scripts/python.exe', '-m', 'pip', 'install', 'SpeechRecognition'])
subprocess.run(['311_venv/Scripts/python.exe', '-m', 'pip', 'install', 'pyaudio'])
subprocess.run(['311_venv/Scripts/python.exe', '-m', 'pip', 'install', 'pyttsx3'])