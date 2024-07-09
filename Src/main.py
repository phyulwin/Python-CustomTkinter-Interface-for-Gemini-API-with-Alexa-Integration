# Python-AI-Personalized-Virtual-Assistant-Project-with-Audio-Integration
from voice_changer import voice_changer
# from alexa import run_alexa

def main():
    try:
        voice_changer()
        # # Main loop to continuously run the virtual assistant
        # while True:
        #     run_alexa()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")


if __name__ == '__main__':
    main()