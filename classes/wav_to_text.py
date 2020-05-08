import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('input.wav') as source:
    audio = r.record(source)

options = r.recognize_google(audio, language="pt-BR", show_all=True)
for prediction in options['alternative']:
        print(" " + prediction["transcript"] + " (" + str(prediction["confidence"]*100) + "%)")

print(options[0], end='\n')