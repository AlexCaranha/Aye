import sys
from plugins.plugin_base import PluginBase

class HandleDocument(PluginBase):
    def get_category_description(self):
        return "Gerenciar documentos."

class HandleFile(PluginBase):
    def get_category_description(self):
        return "Gerenciar arquivos e pastas."

class HandleEmail(PluginBase):
    def get_category_description(self):
        return "Gerenciar emails."

class Knowledge(PluginBase):
    def get_category_description(self):
        return "Pesquisar em fontes como enciclopédias e dicionários."

class Entertainment(PluginBase):
    def get_category_description(self):
        return "Pesquisar músicas, filmes, etc.."

class Internal(PluginBase):
    def get_category_description(self):
        return "Utilitários do sistema, mudar a velocidade de voz"

def get_classes_categories():
    output = dict()
    current_module = sys.modules[__name__]
    
    for key in dir(current_module):
        if isinstance( getattr(current_module, key), type) and key != "PluginBase":
            output[key] = eval(key)

    return output