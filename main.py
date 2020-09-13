
import speech_recognition as sr
import classes.util as util
from plugin_manager import Plugin_Manager

r = sr.Recognizer()
m = sr.Microphone()

manager = Plugin_Manager()
manager.setup_plugin_manager()

try:
    manager.text_to_speech("Silêncio, por favor ...")

    with m as source:
        r.adjust_for_ambient_noise(source)
        print(f"Configurando mínimo limiar para reconhecimento de fala em {r.energy_threshold}")

        while True:
            manager.text_to_speech(manager.get_current_question())
            audio = r.listen(source)

            with open('input.wav', 'wb') as f:
                f.write(audio.get_wav_data())

            # Verificar a energia do sinal.

            
            try:
                # recognize speech using Google Speech Recognition
                input = r.recognize_google(audio, language="pt-BR")

                # we need some special handling here to correctly print unicode characters to standard output
                manager.text_to_speech(f"Você disse: {input}")

                output = manager.run_plugins(input)
                if output is not None:
                    manager.text_to_speech(output)

            except IndexError: # the API key didn't work
                print("No internet connection")

            except LookupError: # speech is unintelligible      
                print("Could not understand audio")

            except sr.UnknownValueError:
                manager.text_to_speech("Comando não reconhecido.")

            except sr.RequestError as e:
                print(f"Uh oh! Não foi possível realizar requisição ao serviço de reconhecimento de fala da Google: {e}")

except KeyboardInterrupt:
    pass