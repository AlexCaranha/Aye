
from manager import Manager

print("starting Beth")
manager = Manager()

print("loading plugins")
manager.load_plugins()

manager.adjust_threshold()

manager.speak("Assistente Beth a seu dispor", is_print=True)

while(manager.is_running() is True):

    (input, error) = manager.listen(is_print=True)

    if (input == "sair"):
        break

print("Assistente Beth finalizada")
