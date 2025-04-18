from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language)
    file_path = "/path/to/audio.mp3"
    tts.save(file_path)
    return file_path
