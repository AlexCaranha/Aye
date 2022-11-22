from gtts import gTTS
from playsound import playsound


def speak(text: str, language: str):
    engine = gTTS(text=text, lang=language, slow=False)
    engine.save("output.mp3")
    playsound('output.mp3')


def set_rate()