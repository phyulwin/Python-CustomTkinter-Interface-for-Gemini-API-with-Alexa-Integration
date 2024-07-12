import tkinter as tk
import customtkinter
import PIL
from PIL import Image

from Utility import print_default_error_message, copy_to_clipboard, exit_program
from Gemini_api import GeminiAPI
from alexa import talk, take_command

class Application:
    # static variables
    WIDTH = 1100 # textbox width

    def __init__(self, root):
        self.root = root
        self.gemini_api = GeminiAPI()
        self.setup_ui()

    def setup_ui(self):
        dialog = customtkinter.CTkInputDialog(text="Type in your Gemini API key: ",
                                              title="Configure Gemini API Key")
        user_api_key = dialog.get_input()  # waits for input
        try:
            if user_api_key:
                self.gemini_api.set_api_key(user_api_key)
        except Exception as e:
            print_default_error_message(e)
            print("Invalid API key. Please try again.")

        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("Assets/application_theme.json")

        self.root.geometry("1262x710")
        self.root.title("Python CustomTkinter Interface for Gemini API with Alexa Integration")

        # Configure app background
        image = PIL.Image.open("Assets/application_background.png")
        background_image = customtkinter.CTkImage(image, size=(1262, 710))

        def bg_resizer(e):
            if e.widget is self.root:
                i = customtkinter.CTkImage(image, size=(e.width, e.height))
                bg_lbl.configure(text="", image=i)

        # Create a background label
        bg_lbl = customtkinter.CTkLabel(self.root, text="", image=background_image)
        bg_lbl.place(x=0, y=0)

        self.root.bind("<Configure>", bg_resizer)
        # Background added!

        # Set prompt input textbox and response output label
        self.prompt_input_frame = customtkinter.CTkTextbox(master=self.root, width=self.WIDTH, height=100)
        self.prompt_input_frame.place(y=400, x=50)

        self.prompt_output_frame = customtkinter.CTkTextbox(master=self.root, width=self.WIDTH, height=300,
                                                            state="disabled")
        self.prompt_output_frame.place(y=50, x=50)

        self.current_response = ""  # global string object

        # Set buttons
        btn_pos_y = 500
        btn_pos_x = 50
        btn_spacing = 170  # width = 150, width + extra spacing

        enter_prompt_btn = customtkinter.CTkButton(master=self.root, text="enter prompt", command=self.request_response)
        enter_prompt_btn.place(y=btn_pos_y, x=btn_pos_x)

        btn_pos_x += btn_spacing
        copy_output_btn = customtkinter.CTkButton(master=self.root, text="copy output", command=self.copy_response)
        copy_output_btn.place(y=btn_pos_y, x=btn_pos_x)

        btn_pos_x += btn_spacing
        voice_input_btn = customtkinter.CTkButton(master=self.root, text="voice input", command=self.voice_input)
        voice_input_btn.place(y=btn_pos_y, x=btn_pos_x)

        btn_pos_x += btn_spacing
        exit_btn = customtkinter.CTkButton(master=self.root, text="exit program", command=exit_program)
        exit_btn.place(y=btn_pos_y, x=btn_pos_x)

        btn_pos_x += btn_spacing
        clear_text_btn = customtkinter.CTkButton(master=self.root, text="new prompt", command=self.clear_text)
        clear_text_btn.place(y=btn_pos_y, x=btn_pos_x)

    def request_response(self):
        try:
            prompt = self.prompt_input_frame.get(0.0, 'end')
            if prompt:  # Check if prompt is not empty
                self.current_response = self.gemini_api.ask_gemini(prompt)
                self.return_response(self.current_response)
        except Exception as e:
            print_default_error_message(e)

    def copy_response(self):
        copy_to_clipboard(self.current_response)

    def voice_input(self):
        self.clear_text()
        talk("detecting sound input")
        command = take_command()
        # display user command in text box
        self.prompt_input_frame.insert(0.0, command)
        self.root.after(100, lambda: self.voice_output(command))

    def voice_output(self, prompt):
        try:
            if prompt:  # Check if command is not empty
                self.current_response = self.gemini_api.ask_gemini(prompt)
                talk(self.current_response)
                self.return_response(self.current_response)
        except Exception as e:
            print_default_error_message(e)

    def clear_text(self):
        self.prompt_input_frame.delete(0.0, tk.END)

    def return_response(self, new_text):
        self.prompt_output_frame.configure(state="normal")
        # delete current response
        if len(self.current_response) != 0:
            self.prompt_output_frame.delete(0.0, tk.END)
        # paste new text
        self.prompt_output_frame.insert(0.0, new_text)
        self.prompt_output_frame.configure(state="disabled")