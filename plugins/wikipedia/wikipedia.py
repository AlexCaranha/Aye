from yapsy.IPlugin import IPlugin
from plugins.categories import Knowledge
import wikipedia as wiki
from fuzzywuzzy import fuzz

class Wikipedia(Knowledge):
    def setup(self):
        self.__activate__(False)

        wiki.set_lang("pt")
        print(f"Wikipedia loaded: ok.")

    def __activate__(self, value):
        self.activated = value

    def search_for_something(self, input: str):
        if input is not None:
            output_list = wiki.search(input)

            output = None
            if output_list is not None:
                output = "Resultados: "
                lista = [f"{i}: {item}" for i, item in enumerate(output_list, start=1)]
                output += ";".join(lista)

            return output

    def search_summary_of(self, input: str):
        if input is not None:
            info = wiki.summary(input)
            return info
            
    def is_the_question(self, pattern, input: str):
        ratio = fuzz.token_set_ratio(pattern, input)
        return ratio > 85

    def is_activated_to_answer_now(self):
        return self.activated

    def get_message_when_plugin_activated_to_answer_now(self):
        return "O que deseja procurar na enciclopédia?"

    def run(self, input):
        if self.activated:
            if self.is_the_question(r'sair da enciclopédia | sair', input):
                self.__activate__(False)
                return "Você saiu da enciclopédia."

            output = self.search_summary_of(input)
            return output
        
        if self.is_the_question(r'procurar na enciclopédia | pesquisar na enciclopédia | enciclopédia', input):
            self.__activate__(True)
            return None

        return None