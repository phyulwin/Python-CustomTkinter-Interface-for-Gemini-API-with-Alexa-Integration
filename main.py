# Python-AI-Personalized-Virtual-Assistant-Project-with-Audio-Integration

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys

# Initialize the speech recognizer
listener = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    """Function to convert text to speech and speak it."""
    engine.say(text)
    engine.runAndWait()


def take_command():
    """Function to listen for commands via microphone and recognize speech."""
    command = ""
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                # Remove 'alexa' from the command if present
                command = command.replace('alexa', '')
                print(command)
    except Exception as e:
        # Print any errors that occur during speech recognition
        print(f"Error recognizing voice: {e}")
    return command


def run_alexa():
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
        talk('Please say the command again.')


# Main loop to continuously run the virtual assistant
while True:
    run_alexa()
