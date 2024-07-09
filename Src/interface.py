import sys
import customtkinter

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

# Create a label within the frame
label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
# Pack the label with padding
label.pack(pady=12, padx=10)

'''
Prompt input and output frames
'''
# Create an entry widget for inputting prompts
prompt_input_frame = customtkinter.CTkEntry(master=frame, placeholder_text="enter prompt here")
# Pack the entry widget with padding
prompt_input_frame.pack(pady=12, padx=10)

# Create an entry widget for displaying output
prompt_output_frame = customtkinter.CTkEntry(master=frame, placeholder_text="output display here")
# Pack the entry widget with padding
prompt_output_frame.pack(pady=12, padx=10)
# Insert new text into the output frame (commented out)
# prompt_output_frame.insert(customtkinter.END, "new_text")
# Disable the output frame to make it read-only
prompt_output_frame.configure(state="disabled")

def login():
    '''
    Placeholder function for the login button
    '''
    print("Test")

def clear_text():
    '''
    Clears the text from the input frame
    '''
    # Get the current input from the input frame
    current_input = prompt_input_frame.get()
    # Clear the current input
    prompt_input_frame.delete(0, len(current_input))

def end_program():
    '''
    Ends the program
    '''
    sys.exit()

'''
Creates buttons
'''
# Create a button to enter the prompt
enter_prompt_btn = customtkinter.CTkButton(master=frame, text="enter prompt", command=login)
# Pack the button with padding
enter_prompt_btn.pack(pady=12, padx=10)

# Create a button to copy the output
copy_output_btn = customtkinter.CTkButton(master=frame, text="copy output", command=login)
# Pack the button with padding
copy_output_btn.pack(pady=12, padx=10)

# Create a button for voice input
voice_input_btn = customtkinter.CTkButton(master=frame, text="voice input", command=login)
# Pack the button with padding
voice_input_btn.pack(pady=12, padx=10)

# Create a button to end the program
exit_btn = customtkinter.CTkButton(master=frame, text="end program", command=end_program)
# Pack the button with padding
exit_btn.pack(pady=12, padx=10)

# Create a button to clear the text
clear_text_btn = customtkinter.CTkButton(master=frame, text="clear text", command=clear_text)
# Pack the button with padding
clear_text_btn.pack(pady=12, padx=10)

# Run the main loop of the application
root.mainloop()
