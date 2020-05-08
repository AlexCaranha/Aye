from yapsy.IPlugin import IPlugin
from plugins.categories import Knowledge
import wikipedia as wiki

class Wikipedia(Knowledge):
    def setup(self):
        wiki.set_lang("pt")

    def run(self, input):
        return wiki.search(input)
