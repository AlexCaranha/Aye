from yapsy.IPlugin import IPlugin
from plugins.categories import Knowledge
from pynput.keyboard import Key, Controller
from fuzzywuzzy import fuzz

class Macro_Keyboard(Knowledge):
    def setup(self, parent):
        self.parent = parent
        self.keyboard = Controller()
        self.__activate__(False)
        print(f"{parent.name} loaded: ok.")

    def __activate__(self, value):
        self.activated = value

    def write(self, sentence:str):
        output = self.keyboard.type(sentence)
        return output

    def is_the_question(self, pattern, input: str):
        ratio = fuzz.token_set_ratio(pattern, input)
        return ratio > 85

    def is_activated_to_answer_now(self):
        return self.activated

    def get_message_when_plugin_activated_to_answer_now(self):
        return "O que deseja escrever?"

    def run(self, input):
        if self.activated:
            if self.is_the_question(r'parar gravação de macro | sair', input):
                self.__activate__(False)
                return "Você saiu do plugin de macro de teclado."

            output = self.write(input)
            return output

        if self.is_the_question(r'gravar macro teclado', input):
            self.__activate__(True)
            return None

        # # It records all the keys until escape is pressed 
        # rk = keyboard.record(until ='Esc') 
        
        # # It replay back the all keys 
        # keyboard.play(rk, speed_factor = 1) 

        return None
