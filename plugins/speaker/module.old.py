import pyttsx3

engine = pyttsx3.init()

voices = []
default_rate = 80


def setup():
    voices = engine.getProperty('voices')
    voices = [voice for voice in voices if "PT-BR" in voice.id or "brazil" in voice.name]
    default_rate = engine.getProperty('rate')


def speak(text: str):
    if len(voices) > 0:
        voice = voices[0]
        engine.setProperty('voice', voice.id)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
