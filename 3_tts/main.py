from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path='mytext.txt'
with open(file_path, 'rt', encoding='UTF-8') as f:
    read_file=f.read()

tts = gTTS(text=read_file, lang='en')
tts.save("hi.mp3")

playsound('hi.mp3')