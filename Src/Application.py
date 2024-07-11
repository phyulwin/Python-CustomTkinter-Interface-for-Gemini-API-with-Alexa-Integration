import tkinter as tk
import customtkinter
from Utility import print_default_error_message, copy_to_clipboard, exit_program
from gemini import askGemini
from alexa import talk, take_command

class Application:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        customtkinter.set_appearance_mode("light")
        customtkinter.set_default_color_theme("dark-blue")

        self.root.geometry("960x540")

        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.prompt_input_frame = customtkinter.CTkEntry(master=frame, placeholder_text="enter prompt here",
                                                        width=200, height=150)
        self.prompt_input_frame.pack(pady=12, padx=10)

        self.prompt_output_frame = customtkinter.CTkLabel(master=frame, text="display out here", font=("Roboto", 11))
        self.prompt_output_frame.pack(pady=12, padx=10)

        self.current_response = ""

        enter_prompt_btn = customtkinter.CTkButton(master=frame, text="enter prompt", command=self.request_response)
        enter_prompt_btn.pack(pady=12, padx=10)

        copy_output_btn = customtkinter.CTkButton(master=frame, text="copy output", command=self.copy_response)
        copy_output_btn.pack(pady=12, padx=10)

        voice_input_btn = customtkinter.CTkButton(master=frame, text="voice input", command=self.voice_input)
        voice_input_btn.pack(pady=12, padx=10)

        exit_btn = customtkinter.CTkButton(master=frame, text="exit program", command=exit_program)
        exit_btn.pack(pady=12, padx=10)

        clear_text_btn = customtkinter.CTkButton(master=frame, text="new prompt", command=self.clear_text)
        clear_text_btn.pack(pady=12, padx=10)

    def request_response(self):
        try:
            prompt = self.prompt_input_frame.get()
            if prompt:  # Check if prompt is not empty
                response = askGemini(prompt)
                self.current_response = response
                self.return_response(response)
        except Exception as e:
            print_default_error_message(e)

    def copy_response(self):
        copy_to_clipboard(self.current_response)

    def voice_input(self):
        self.clear_text()
        talk("detecting sound input")
        command = take_command()
        self.prompt_input_frame.insert(0, command)
        self.root.after(100, lambda: self.voice_output(command))

    def voice_output(self, command):
        try:
            if command:  # Check if command is not empty
                response = askGemini(command)
                self.current_response = response
                talk(response)
                self.return_response(response)
        except Exception as e:
            print_default_error_message(e)

    def clear_text(self):
        self.prompt_input_frame.delete(0, tk.END)

    def return_response(self, new_text):
        self.prompt_output_frame.configure(text=new_text)

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = Application(root)
    try:
        root.mainloop()
    except Exception as e:
        print_default_error_message(e)
