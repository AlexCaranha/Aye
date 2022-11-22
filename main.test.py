import random
import time

from plugins.core import listen

if __name__ == "__main__":
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 200

    microphone = sr.Microphone()

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

    while (True):
        print("Hello, how can I help you?")
        sentence = recognize_speech_from_mic(
            recognizer, microphone)

        print(f"You said: {sentence}")

        if "exit" in sentence or "quit" in sentence:
            break
