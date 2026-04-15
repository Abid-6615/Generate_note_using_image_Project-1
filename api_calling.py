from google import genai
from PIL import Image
import os, io
from gtts import gTTS
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

my_api_key = os.getenv("GENIMI_API_KEY")

client = genai.Client(api_key=my_api_key)


# Note generator
def note_genetator(images):
    prompt = """Summarize the picture in note formate at max 150 words
                make sure to add necessary markdown to differentiate diffrent section"""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= [images, prompt]
    )
    return response.text

# Audio generator
def audio_transcription(text):
    speech = gTTS(text, lang = 'en', slow = False)
    speech.save("welcome.mp3")
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer

# Quiz_generator
def quiz_generator(image, difficulty):
    prompt = """Generate 3 quizzes based on the {difficulty}. 
                Make sure to add markdown to differentiate the options
                and add correct answer"""
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= [image, prompt]
    )
    return response.text