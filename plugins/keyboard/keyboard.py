from yapsy.IPlugin import IPlugin
from plugins.categories import Internal
import plugins.keyboard.module as module
from fuzzywuzzy import fuzz

class Keyboard(Internal):
    def setup(self):
        self.activated = False
        print(f"Keyboard loaded: ok.")

    def write(self, sentence:str):
        return module.write_sentence(sentence)

    def is_the_question(self, pattern, input: str, ratio_threshold = 85):
        ratio = fuzz.token_set_ratio(pattern, input)
        return ratio > ratio_threshold

    def is_activated_to_answer_now(self):
        return self.activated

    def get_message_when_plugin_activated_to_answer_now(self):
        return "O que deseja escrever?"

    def commands_in_normal_mode(self, input):
        if self.is_the_question(r'comando novo parágrafo', input):
            return module.new_paragraph()

        if self.is_the_question(r'comando selectionar texto', input):
            return module.select_all()

        if self.is_the_question(r'comando cursor no início do texto', input):
            return module.go_to_start_position()

        if self.is_the_question(r'comando cursor no fim do texto', input):
            return module.go_to_end_position()

        output = self.write(input)
        return output

    def is_waiting_press_enter(self):
        """
        Press enter to exit waiting mode.
        """
        input("Press Enter to continue...")

    def run(self, input):
        if self.activated:
            if self.is_the_question(r'sair do modo escrita', input, 95):
                self.activated = False
                return "Você saiu do plugin de escrever."

            return self.commands_in_normal_mode(input)

        if self.is_the_question(r'entrar no modo escrita', input, 95):
            self.activated = True
            return None

        return None
