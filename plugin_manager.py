
from plugins.categories import get_classes_categories
from yapsy.PluginManager import PluginManager
import classes.util as util

class Plugin_Manager:    
    def setup_plugin_manager(self):
        self.initial_question = "O que você deseja?"
        self.current_question = [self.initial_question]

        self.manager = PluginManager()
        self.manager.setCategoriesFilter(get_classes_categories())
        self.manager.setPluginPlaces(["plugins"])
        self.manager.collectPlugins()

        plugins = self.manager.getAllPlugins()
        for plugin in plugins:
            self.setup_plugin(plugin)

    def get_categories(self):
        output = self.manager.getCategories()
        return output

    def get_plugins_of_category(self, category_name):
        output = self.manager.getPluginsOfCategory(category_name)    
        return output

    def get_plugin_by_name(self, plugin_name, category_name):
        output = self.manager.getPluginByName(plugin_name, category_name)
        return output

    def get_plugin_class_by_name(self, plugin_name, category_name):
        output = self.manager.getPluginByName(plugin_name, category_name)

        if output == None:
            return None

        return output.plugin_object

    def get_plugin_info(self, plugin):
        categories = ", ".join([category for category in plugin.categories if category != "Plugin"])
        output = f"plugin: {plugin.name}\n" + \
                f"categories: {categories}\n" + \
                f"author: {plugin.author}\n" + \
                f"description: {plugin.description}."

        return output

    def setup_plugin(self, plugin):
        plugin.plugin_object.setup(parent=plugin)

    def run_plugin(self, plugin, sentence):
        output = plugin.plugin_object.run(sentence)
        return output

    def run_plugins(self, input):
        plugins = self.manager.getAllPlugins()

        plugins_activated = []
        output = []

        for plugin in plugins:
            message = self.run_plugin(plugin, sentence=input)

            if message is not None:
                output.append(f"{plugin.name} retornou: {message}")
                
            if plugin.plugin_object.is_activated_to_answer_now():
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
                message = plugin.plugin_object.get_message_when_plugin_activated_to_answer_now()

                if util.isNotBlank(message):
                    output.append(message)

            if util.isBlank(output):
                output = [self.initial_question]

            return output

        output = [self.initial_question]
        return output

    def get_current_question(self):
        return ".".join(self.current_question)

    # def text_to_speech(self, text, language="pt"):
    #     print(text)
    #     vocoder_plugin = self.get_plugin_by_name("Vocoder", "Internal")
    #     util.text_to_speech(text, vocoder_plugin, language)

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