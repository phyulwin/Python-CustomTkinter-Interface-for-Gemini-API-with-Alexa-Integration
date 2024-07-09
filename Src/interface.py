
from tkinter import *
import customtkinter

from Utility import print_default_error_message, copy_to_clipboard, exit_program
from gemini import askGemini
from alexa import talk, take_command
'''
Set up environment variables
'''
# Set the appearance mode to "light"
customtkinter.set_appearance_mode("light")
# Set the default color theme to "dark-blue"
customtkinter.set_default_color_theme("dark-blue")

# Create the main application window
root = customtkinter.CTk()
# Set the size of the window
root.geometry("960x540")

# Create a frame within the main window
frame = customtkinter.CTkFrame(master=root)
# Pack the frame with padding and allow it to expand
frame.pack(pady=20, padx=60, fill="both", expand=True)

RESPONSE = "empty string variable"

'''
Prompt input and output frames
'''
# Create an entry widget for inputting prompts
prompt_input_frame = customtkinter.CTkEntry(master=frame, placeholder_text="enter prompt here",
                                            width=200, height=150)
# Pack the entry widget with padding
prompt_input_frame.pack(pady=12, padx=10)

# Create an entry widget for displaying output
prompt_output_frame = customtkinter.CTkLabel(master=frame, text="display out here", font=("Roboto", 11))
# Pack the entry widget with padding
prompt_output_frame.pack(pady=12, padx=10)

def request_response():
    try:
        # get prompt from user
        prompt = prompt_input_frame.get()
        if len(prompt) != 0:
            # ask gemini and display output
            response = askGemini(prompt)
            # RESPONSE = response #TODO
            return_response(response)
    except Exception as e:
        print_default_error_message(e)

def copy_response():
    copy_to_clipboard(RESPONSE) #TODO - NOT PROPERLY WORKING

def voice_input():
    talk("detecting sound input")
    command = take_command()
    # prompt_input_frame.insert(0, command)
    try:
        if len(command) != 0:
            # ask gemini and display output
            response = askGemini(command)
            # RESPONSE = response #TODO
            return_response(response)
            talk(response) #TODO - FIX PROGRAM NOT RESPONDING HERE
    except Exception as e:
        print_default_error_message(e)

def clear_text():
    '''
    Clears the text from the input frame
    '''
    # Get the current input from the input frame
    current_input = prompt_input_frame.get()
    # Clear the current input
    prompt_input_frame.delete(0, len(current_input))

def return_response(new_text):
    prompt_output_frame.configure(text=new_text)

'''
Creates buttons
'''
# Create a button to enter the prompt
enter_prompt_btn = customtkinter.CTkButton(master=frame, text="enter prompt", command=request_response)
# Pack the button with padding
enter_prompt_btn.pack(pady=12, padx=10)

# Create a button to copy the output
copy_output_btn = customtkinter.CTkButton(master=frame, text="copy output", command=copy_response)
# Pack the button with padding
copy_output_btn.pack(pady=12, padx=10)

# Create a button for voice input
voice_input_btn = customtkinter.CTkButton(master=frame, text="voice input", command=voice_input)
# Pack the button with padding
voice_input_btn.pack(pady=12, padx=10)

# Create a button to end the program
exit_btn = customtkinter.CTkButton(master=frame, text="exit program", command=exit_program)
# Pack the button with padding
exit_btn.pack(pady=12, padx=10)

# Create a button to clear the text
clear_text_btn = customtkinter.CTkButton(master=frame, text="new prompt", command=clear_text)
# Pack the button with padding
clear_text_btn.pack(pady=12, padx=10)

try:
    # Run the main loop of the application
    root.mainloop()
except Exception as e:
    print_default_error_message(e)