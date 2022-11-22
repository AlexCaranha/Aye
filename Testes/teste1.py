import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

for voice in voices:
    print(voice.id, voice.name, voice.languages)


engine.setProperty("voice", "english")
engine.say("Good night my friend.")
engine.runAndWait()


engine.setProperty("voice", "brazil")
engine.say("Boa noite meu amigo.")
engine.runAndWait()
