import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key = os.getenv('API_KEY'))

file_path = "../audio/Sample_Audio_EN.wav"

audio_file = open(file_path, "rb")

transcription = client.audio.transcriptions.create(model = "whisper-1", file = audio_file)

print(transcription.text)