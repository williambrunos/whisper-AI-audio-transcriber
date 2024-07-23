from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
audio_file = open("your_audio_file", "rb")

transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text",
  language="pt" # Change to the language of the audio file
)

# Salvar a transcrição em um arquivo .txt
with open("transcricao.txt", "w", encoding="utf-8") as file:
    file.write(transcription)

print("Transcrição salva em transcricao.txt")