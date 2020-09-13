
# from win32com.client import Dispatch

# speak = Dispatch("SAPI.SpVoice")

# speak.Speak("Você saiu da enciclopédia")

# ======================================

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)

for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("I will speak this text")
    engine.say("Eu vou falar este texto")
    engine.runAndWait()
    engine.stop()

engine.save_to_file("How do you do?", "output.mp3")

# ======================================
# import pyttsx3;

# engine = pyttsx3.init()
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate+50)
# engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

# ======================================
# import pyttsx3

# # engine = pyttsx3.init()
# engine = pyttsx3.init(driverName='sapi5') 
# voices = engine.getProperty('voices')

# for voice in voices:
#     print(voice)
#     engine.setProperty('voice', voice.id)
#     break

# engine.say('Olá mundo.')
# engine.say('Procurar na enciclopédia.')
# engine.runAndWait()

# ======================================
# import gtts
# print(gtts.lang.tts_langs())
# ======================================