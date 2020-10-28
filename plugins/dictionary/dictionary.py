
from yapsy.IPlugin import IPlugin
from plugins.categories import Knowledge
from plugins.dictionary.module import get_definition

from fuzzywuzzy import fuzz
import re

class Dicionary(Knowledge):
    def setup(self):
        print(f"Dicionary loaded: ok.")
        self.activated = False

    def is_activated_to_answer_now(self):
        return self.activated

    def is_the_question_with_sentence(self, pattern, input: str):
        match = re.search(pattern, input, re.IGNORECASE)
        return match.group('sentence') if match is not None else None

    def is_the_question(self, pattern, input: str):
        ratio = fuzz.token_set_ratio(pattern, input)
        return ratio > 85

    def get_message_when_plugin_activated_to_answer_now(self):
        return "Qual palavra deseja consultar a definição?"

    def run(self, input):
        if not self.activated:
            if self.is_the_question(r'dicionário', input):
                self.activated = True
                return "Dicionário ativado."

            return None

        if self.is_the_question(r'sair do dicionário', input):
            self.activated = False
            return "Dicionário desativado."

        word = self.is_the_question_with_sentence(r'a palavra (?P<word>.*)%', input)
        if word is not None:
            value = get_definition(input)            
            return value
        
        value = get_definition(input)
        return value
