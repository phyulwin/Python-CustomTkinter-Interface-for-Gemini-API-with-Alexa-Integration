import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the environment variables from the .env file
load_dotenv()

# genai.configure(api_key=os.environ['API_KEY'])
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

def askGemini(prompt):
    if(len(prompt)!=0):
        response = model.generate_content(prompt)
        print(response.text)



'''
more features: https://github.com/google-gemini/cookbook/blob/main/quickstarts/Prompting.ipynb
'''