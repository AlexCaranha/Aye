
from yapsy.IPlugin import IPlugin
from plugins.categories import Internal
from fuzzywuzzy import fuzz

class Core(Internal):
    def setup(self, parent):
        self.parent = parent        

        self.is_it_waiting = False
        self.is_it_exiting = False

        print(f"{parent.name} loaded: ok.")

    def is_the_question(self, pattern, input: str):
        # ratio = fuzz.token_set_ratio(pattern, input)
        # return ratio > threshold
        options = pattern.split(" | ")
        status = len(list(filter(lambda o : o.lower() == input.lower(), options))) > 0
        return status

    def is_activated_to_answer_now(self):
        return True

    def get_message_when_plugin_activated_to_answer_now(self):
        return ""

    def commands_in_waiting_mode(self, input):
        if self.is_the_question(r'Beth acordar | Acordar assistente', input):
            return self.mode_waiting_off()

        print(input)
        return None

    def turning_off(self):
        self.is_it_exiting = True
        return f"Estou sendo desligada. Até logo."

    def mode_waiting_on(self):
        self.is_it_waiting = True
        return "Bete entrou em modo de espera. Pressione enter para sair do modo de espera."

    def mode_waiting_off(self):
        self.is_it_waiting = False
        return "Bete saiu do modo de espera."

    def commands_in_normal_mode(self, input):
        if self.is_the_question(r'Beth desligar | Desligar assistente', input):
            return self.turning_off()

        if self.is_the_question(r'Beth dormir | Beth suspender | Beth esperar | Suspender assistente', input):
            return self.mode_waiting_on()

        return None

    def run(self, input):
        if self.is_it_waiting:
            return self.commands_in_waiting_mode(input)

        return self.commands_in_normal_mode(input)
