# Says hello: https://pypi.org/project/pyttsx3/

import pyttsx3

engine = pyttsx3.init()
name = input("What's your name? ")
engine.say(f"hello, {name}")
engine.runAndWait()
