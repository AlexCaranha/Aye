
from plugins.categories import get_classes_categories
import classes.util as util 

from plugins.core.core import Core
from plugins.speaker.speaker import Speaker
from plugins.clock.clock import Clock
from plugins.dictionary.dictionary import Dicionary
from plugins.keyboard.keyboard import Keyboard
from plugins.translate.translate import Translate
from plugins.wikipedia.wikipedia import Wikipedia

class Plugin_Manager:
    def setup_plugin_manager(self):
        self.initial_question = "O que você deseja?"
        self.current_question = [self.initial_question]

        self.plugins = [Core(), Speaker(), Clock(), Dicionary(), Keyboard(), Translate(), Wikipedia()]
        for plugin in self.plugins:
            plugin.setup()

    def get_plugin_class_by_name(self, plugin_name, category_name):
        output = [plugin for plugin in self.plugins if plugin.__class__.__name__ == plugin_name]

        if output == None:
            return None

        return output[0]

    def run_plugins(self, input):
        plugins_activated = []
        output = []

        for plugin in self.plugins:
            message = plugin.run(input)

            if message is not None:
                plugin_name = plugin.__class__.__name__
                output.append(f"{plugin_name} retornou: {message}")
                
            if plugin.is_activated_to_answer_now():
                plugins_activated.append(plugin)

        self.current_question = self.get_current_messages(plugins_activated)

        if len(output) == 0 and len(plugins_activated) == 0:
            return "comando não identificado."

        if len(output) > 0:
            return ".".join(output)

        return None

    def get_current_messages(self, plugins_activated:list):
        if len(plugins_activated) > 0:
            output = list()

            for plugin in plugins_activated:
                message = plugin.get_message_when_plugin_activated_to_answer_now()

                if util.is_not_blank(message):
                    output.append(message)

            if util.is_blank(output):
                output = [self.initial_question]

            return output

        output = [self.initial_question]
        return output

    def get_current_question(self):
        return ".".join(self.current_question)


# Translate
# plugin = get_plugin_by_name("Translate", "Knowledge", plugin_manager)
# run_plugin(plugin, "translate to portuguese the sentence what is your name")
# run_plugin(plugin, "traduzir para o inglês a frase qual é seu nome")

# Wikipedia
# plugin = get_plugin_by_name("Wikipedia", "Knowledge", plugin_manager)
# run_plugin(plugin, "procurar na enciclopedia sobre Vinicius de")
# run_plugin(plugin, "procurar na enciclopedia resumo sobre Vinicius de Moraes")

# Pendrive
# plugin = get_plugin_by_name("Pendrive", "HandleFile", plugin_manager)
# run_plugin(plugin, "localizar pendrive")

# Gmail
# plugin = get_plugin_by_name("Gmail", "HandleEmail", plugin_manager)
# run_plugin(plugin, "enviar email com título Olá e mensagem Oi Mundo")

# Explorer
# parei aqui.