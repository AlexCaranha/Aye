import sys
from abc import ABC, abstractmethod

class Plugin(ABC):
    @abstractmethod
    def get_category_description(self):
        return

    @abstractmethod
    def setup(self):
        return

    @abstractmethod
    def run(self, input):
        return

class HandleFile(Plugin):
    def get_category_description(self):
        return "Gerenciar arquivos e pastas."

class Knowledge(Plugin):
    def get_category_description(self):
        return "Pesquisar em fontes como enciclopédias e dicionários."

class Entertainment(Plugin):
    def get_category_description(self):
        return "Pesquisar músicas, filmes, etc.."

def get_classes_categories():
    output = dict()
    current_module = sys.modules[__name__]
    for key in dir(current_module):
        if isinstance( getattr(current_module, key), type ) and key != 'Plugin':            
            output[key] = eval(key)

    return output