import sys
import requests

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