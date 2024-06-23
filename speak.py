import subprocess
import sys



if len(sys.argv) >= 2:
    input_data = sys.argv[1]

engine = pyttsx3.init()
engine.say(input_data)
engine.runAndWait()
