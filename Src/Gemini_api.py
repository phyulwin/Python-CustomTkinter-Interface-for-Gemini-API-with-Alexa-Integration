import google.generativeai as genai
from Utility import print_default_error_message


class GeminiAPI:
    def __init__(self):
        self.api_key = ""
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def set_api_key(self, new_key):
        try:
            genai.configure(api_key=new_key)
        except Exception as e:
            print("Invalid API key")
            print_default_error_message(e)

    def set_genai_custom_model(self, new_model):
        try:
            self.model = genai.GenerativeModel(new_model)
        except Exception as e:
            print("Invalid model")
            print_default_error_message(e)

    def ask_gemini(self, prompt):
        try:
            if len(prompt) != 0:
                response = self.model.generate_content(prompt)
                return response.text
        except Exception as e:
            print_default_error_message(e)
