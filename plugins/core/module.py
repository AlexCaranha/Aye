
import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 200

m = sr.Microphone()

def listen(phrase_time_limit = None):
    error = None
    try:
        with m as source:
            if phrase_time_limit is None:
                audio = r.listen(source)
            else:
                audio = r.listen(source, phrase_time_limit=phrase_time_limit)

            try:
                message = r.recognize_google(audio, language="pt-BR")

            except IndexError: # the API key didn't work
                message = None
                error = "No internet connection"

            except LookupError: # speech is unintelligible
                message = None
                error = "Could not understand audio"

            except sr.UnknownValueError:
                message = None
                error = "Comando não reconhecido."

            except sr.RequestError as e:
                message = None
                error = f"Não foi possível realizar requisição ao serviço de reconhecimento de fala da Google: {e}"

    except KeyboardInterrupt:
        error = "Interrupt by user."
        pass

    return (message, error)


def adjust_threshold():
    """
    Adjust threshold to identify user's commands.
    """
    with m as source:
        r.adjust_for_ambient_noise(source)

    print(f"Configurado limiar mínimo para reconhecimento de fala: {r.energy_threshold}")
