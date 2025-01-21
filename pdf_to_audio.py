import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
import pyttsx3 # type: ignore
from PyPDF2 import PdfReader, PdfWriter # type: ignore
import os
import fitz # type: ignore
from gtts import gTTS # type: ignore


url = 'https://www.bbc.com/news'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('h2')

    for headline in headlines:
        print(headline.text)
else:
    print(f"Failed to retrieve the page. Status code:{response.status_code}")



#pdf to speech

file_name = 'audio.pdf'
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text
def text_to_audio(text, audio_path):
    if not text.strip():
        print("No text found in the PDF!")
        return
    tts = gTTS(text, lang='en')
    tts.save(audio_path)
    print(f"Audio saved as: {audio_path}")
pdf_text = extract_text_from_pdf(file_name)
audio_file_path = 'file.mp3'
if pdf_text:
    text_to_audio(pdf_text, audio_file_path)
else:
    print("Failed to extract text from the PDF.")

if os.path.exists(audio_file_path):
    print(f"Audio file successfully created at: {os.path.abspath(audio_file_path)}")
else:
    print("Failed to create the audio file.")