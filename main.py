
import speech_recognition as sr
import classes.util as util
from plugin_manager import Plugin_Manager

r = sr.Recognizer()
m = sr.Microphone()

manager = Plugin_Manager()
manager.setup_plugin_manager()

try:
    speaker.speak("Iniciando assistente Beth")
    core = manager.get_plugin_class_by_name("Core", "Internal")
    speaker = manager.get_plugin_class_by_name("Speaker", "Internal")
    keyboard = manager.get_plugin_class_by_name("Keyboard", "Internal")

    with m as source:
        r.adjust_for_ambient_noise(source)
        print(f"Configurado limiar mínimo para reconhecimento de fala: {r.energy_threshold}")

        while True:
            speaker.speak(manager.get_current_question())
            audio = r.listen(source)

            # Verificar a energia do sinal.
            # TODO: A FAZER.
            
            try:
                # recognize speech using Google Speech Recognition
                input = r.recognize_google(audio, language="pt-BR")                

                speaker.speak_what_i_say(input)
                output = core.run(input)

                if util.isNotBlank(output):
                    if core.is_it_exiting:                    
                        speaker.speak(output)
                        speaker.activated = False
                        break

                    if core.is_it_waiting:                        
                        speaker.speak(output)
                        speaker.activated = False                        

                        keyboard.is_waiting_press_enter()

                        speaker.activated = True
                        core.mode_waiting_off()
                        continue
                    else:
                        speaker.speak(output)
                        speaker.activated = core.activated

                if input == "comando configurar som ambiente":
                    r.adjust_for_ambient_noise(source)
                    speaker.speak(f"Silêncio configurado com sucesso. Limiar em {r.energy_threshold}.")
                    continue

                output = manager.run_plugins(input)
                if output is not None:
                    speaker.speak(output)                

            except IndexError: # the API key didn't work
                print("No internet connection")

            except LookupError: # speech is unintelligible      
                print("Could not understand audio")

            except sr.UnknownValueError:
                speaker.speak("Comando não reconhecido.")

            except sr.RequestError as e:
                print(f"Uh oh! Não foi possível realizar requisição ao serviço de reconhecimento de fala da Google: {e}")

except KeyboardInterrupt:
    pass