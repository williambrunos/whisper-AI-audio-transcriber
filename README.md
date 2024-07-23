# Whisper AI transcriber

This project has the objective to ilustrate how to perform an audio transcription using the Whisper AI model from OpenAI.

Further read: [Introducing Whisper AI](https://openai.com/index/whisper/)

## How to set up the project locally

1. Clone the project:

````bash
git clone https://github.com/williambrunos/whisper-AI-audio-transcriber.git
````

2. Open the project locally
3. Rename the `.env.example` file to `.env`
4. Fill the value of the property `OPENAI_API_KEY` in the `.env` file with your own openai key

You can see how to set up an openai key in this tutorial:

[OpenAI Quickstart](https://platform.openai.com/docs/quickstart)

5. Set up a python venv

````bash
python -m venv venv
````

6. Activate the venv with one of the following commands

For windows cmd

````bash
venv\Scripts\activate
````

For windows powershell

````bash
venv\Scripts\Activate.ps1
````

For linux and mac os

````bash
venv\Scripts\activate.bat
````


7. Install the dependencies in the venv

````bash
pip install -r requirements.txt
````

8. Run the project

````bash
python main.py
````