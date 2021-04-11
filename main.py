
from manager import Manager

print("starting Beth")
manager = Manager()

print("loading plugins")
manager.load_plugins()

manager.adjust_threshold()

manager.speak("Assistente a seu dispor", is_print=True)

while(manager.is_running() is True):

    (input, error) = manager.listen_from_microphone()

    if (input != None and error == None):
        manager.speak(input, is_print=True)
    else:
        manager.speak("Erro: " + error, is_print=True)
        continue

    if (input == "sair"):
        break

manager.speak("Até a próxima.", is_print=True)
