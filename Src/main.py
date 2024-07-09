# Python-AI-Personalized-Virtual-Assistant-Project-with-Audio-Integration

from interface import setup_interface
from voice_changer import voice_changer
from alexa import greet
# from alexa import run_alexa

def main():
    try:
        setup_interface()
        greet()
        # voice_changer()
        # copy_to_clipboard("Hello, this text is now on your clipboard!")
        # # Main loop to continuously run the virtual assistant
        # while True:
        #     run_alexa()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")


if __name__ == '__main__':
    main()
