import sys
import requests
import keyboard
import pyperclip

'''
This function checks whether the system or device has a consistently stable internet connection, as it's crucial for the API-dependent program to operate effectively.
The function will halt the program if there is no internet connection available.
'''
def check_internet():
    try:
        response = requests.get('http://www.google.com', timeout=5)
        print("Internet is connected")
    except requests.ConnectionError:
        print("Internet is not connected")
        sys.exit()

def print_default_error_message(e):
    print(f'An unexpected error occurred: {e}')

def on_key_event(event):
    print(f"Key {event.name} pressed")
    # Call your function here
    your_function()

def your_function():
    print("Your function has been called!")

# # Set up a listener for a specific key, e.g., the 'a' key
# keyboard.on_press_key("a", on_key_event)
#
# print("Press 'a' to call the function. Press 'esc' to exit.")
#
# # Keep the script running
# keyboard.wait('esc')

def copy_to_clipboard(text):
    pyperclip.copy(text)

def exit_program():
    '''
    Ends the program
    '''
    sys.exit()