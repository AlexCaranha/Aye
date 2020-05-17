
import speech_recognition as sr
import classes.util as util
# import comandos
import plugin_manager as manager

r = sr.Recognizer()
m = sr.Microphone()

try:
    util.text_to_speach("Silêncio, por favor ...")

    with m as source:
        r.adjust_for_ambient_noise(source)
        # print(f"Configurando mínimo limiar para reconhecimento de fala em {r.energy_threshold}")
        
        while True:
            util.text_to_speach("O que você deseja?")
            audio = r.listen(source)

            with open('input.wav', 'wb') as f:
                f.write(audio.get_wav_data())
            
            try:
                # recognize speech using Google Speech Recognition
                input = r.recognize_google(audio, language="pt-BR")

                # we need some special handling here to correctly print unicode characters to standard output
                util.text_to_speach(f"Você disse: {input}")

                output = manager.run_plugins(input)
                util.text_to_speach(output)

            except sr.UnknownValueError:
                util.text_to_speach("Comando não reconhecido.")

            except sr.RequestError as e:
                print(f"Uh oh! Não foi possível realizar requisição ao serviço de reconhecimento de fala da Google: {e}")

except KeyboardInterrupt:
    pass