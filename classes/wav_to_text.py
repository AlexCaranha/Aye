import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('input.wav') as source:
    audio = r.record(source)

output = r.recognize_google(audio, language="pt-BR")

print(output)
