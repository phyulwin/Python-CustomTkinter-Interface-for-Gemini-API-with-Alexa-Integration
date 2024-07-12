# Python CustomTkinter Interface for Gemini API with Alexa Integration

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Description
This application provides a Custom Tkinter GUI interface for interacting with the Gemini API using both text and voice inputs, with responses displayed in the UI. It demonstrates basic GUI setup, event handling, and integration with external APIs and utilities.

## Features
- Prompt Input
- Copy Output
- Voice Input
- Exit Program
- New Prompt

## Screenshots
![Screenshot](https://github.com/phyulwin/Python-CustomTkinter-Interface-for-Gemini-API-with-Alexa-Integration/blob/master/Assets/Screenshot%20(1488).png)
![Screenshot](https://github.com/phyulwin/Python-CustomTkinter-Interface-for-Gemini-API-with-Alexa-Integration/blob/master/Assets/Screenshot%20(1489).png)

## Installation
Clone the repository. Create and activate a virtual environment. Install the required libraries: ```pip install -r requirements.txt```
Prerequisites needed to run the project:
- Python3
- `tkinter`
- `customtkinter`
- `Pillow`
- `speech_recognition`
- `pyttsx3`
- `pywhatkit`
- `wikipedia`
- `pyjokes`
- `google-generativeai`

### Installation Steps
Detailed steps to install the project and its dependencies.

1. Clone the repository
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. Create and activate a virtual environment (optional but recommended)
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required libraries
    ```bash
    pip install tkinter customtkinter Pillow speechrecognition pyttsx3 pywhatkit wikipedia pyjokes google-generativeai
    ```

4. Install additional dependencies from the requirements file (if applicable)
    ```bash
    pip install -r requirements.txt
    ```

### Example command to run the project
```python main.py```

## Contributing
This project was created for educational purposes. Contributions are welcomed! 

- Fork the repository
- Create your feature branch (git checkout -b feature/AmazingFeature)
- Commit your changes (git commit -m 'Add some AmazingFeature')
- Push to the branch (git push origin feature/AmazingFeature)
- Open a Pull Request

## Acknowledgements
Thank you to the individuals whose code has been referenced and used to this project's development. I also appreciate the inspiration from various sources that guided me in shaping this project. Lastly, I acknowledge the assets and references that provided essential insights and knowledge throughout my work.

###### Finally, thank you for checking my project, and I hope you're doing well! Just a quick note—if the API service we're using stops, the program should automatically switch to a fallback mode. This will ensure that core functionalities continue to work using cached data or alternative sources. You might notice some limited features, and there will be messages to inform users about it.