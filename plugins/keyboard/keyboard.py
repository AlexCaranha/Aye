from yapsy.IPlugin import IPlugin
from plugins.categories import Internal
from pynput.keyboard import Key, Controller
from fuzzywuzzy import fuzz

class Keyboard(Internal):
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

    def is_the_question(self, pattern, input: str, ratio_threshold = 85):
        ratio = fuzz.token_set_ratio(pattern, input)
        return ratio > ratio_threshold

    def is_activated_to_answer_now(self):
        return self.activated

    def get_message_when_plugin_activated_to_answer_now(self):
        return "O que deseja escrever?"

    def commands_in_normal_mode(self, input):
        if self.is_the_question(r'novo parágrafo', input):
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)

            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)
            return "Enter pressionado duas vezes."

        output = self.write(input)
        return output

    def is_waiting_press_enter(self):
        # The event listener will be running in this block
        input("Press Enter to continue...")

    def run(self, input):
        if self.activated:
            if self.is_the_question(r'sair do modo escrita', input, 95):
                self.__activate__(False)
                return "Você saiu do plugin de escrever."

            return self.commands_in_normal_mode(input)

        if self.is_the_question(r'entrar no modo escrita', input, 90):
            self.__activate__(True)
            return None

        return None
