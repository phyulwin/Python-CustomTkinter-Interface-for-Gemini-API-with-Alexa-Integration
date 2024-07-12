# Python-AI-Personalized-Virtual-Assistant-Project-with-Audio-Integration
from Utility import check_internet, print_default_error_message
check_internet()

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

from gemini import askGemini

# Initialize the speech recognizer
listener = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    try:
        """Function to convert text to speech and speak it."""
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print_default_error_message(e)

def take_command():
    """Function to listen for commands via microphone and recognize speech."""
    command = ""
    try:
        with sr.Microphone() as source:
            # print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                # Remove 'alexa' from the command if present
                command = command.replace('alexa', '')
                print('User: ', command)
    except Exception as e:
        # Print any errors that occur during speech recognition
        print_default_error_message(e)
    return command

def greet():
    talk('Hi! What can I do for you?')

def run_alexa():
    try:
        """Function to execute commands based on recognized speech."""
        command = take_command()
        print(command)
        if 'play' in command:
            # Play a song on YouTube
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            # Get and speak the current time
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'tell me about' in command:
            # Get and speak information from Wikipedia about a person
            person = command.replace('tell me about', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'joke' in command:
            # Tell a joke
            talk(pyjokes.get_joke())
        elif 'stop' in command:
            # Stop the program when 'stop' command is recognized
            print('stopping the program')
            sys.exit()
        else:
            # Ask user to repeat the command if none of the recognized commands are found
            askGemini(command)
            talk('Please say the command again.')
    except Exception as e:
        print_default_error_message(e)
