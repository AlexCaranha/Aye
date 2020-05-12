from yapsy.IPlugin import IPlugin
from plugins.categories import Knowledge
import wikipedia as wiki
import re

class Wikipedia(Knowledge):
    def setup(self, parent):
        self.parent = parent
        wiki.set_lang("pt")
        print(f"{parent.name} loaded: ok.")

    def is_the_question(self, pattern, input: str):
        match = re.search(pattern, input, re.IGNORECASE)
        return match.group('sentence') if match is not None else None

    def search_for_something(self, input: str):
        if input is not None:
            info = wiki.search(input)
            print(info)

    def search_summary_of(self, input: str):
        if input is not None:
            info = wiki.summary(input)
            print(info)

    def run(self, input):
        # Search for something
        sentence = self.is_the_question(r'procurar na enciclopedia sobre (?P<sentence>.*)', input)
        if sentence is not None:
            self.search_for_something(sentence)
            return

        # Search summary of ...
        sentence = self.is_the_question(r'procurar na enciclopedia resumo sobre (?P<sentence>.*)', input)
        if sentence is not None:
            self.search_summary_of(sentence)
            return