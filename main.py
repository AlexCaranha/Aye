
from plugins.categories import get_classes_categories
from yapsy.PluginManager import PluginManager

def setup_plugin_manager():    
    manager = PluginManager()
    manager.setCategoriesFilter(get_classes_categories())
    manager.setPluginPlaces(["plugins"])
    manager.collectPlugins()

    plugins = manager.getAllPlugins()
    for plugin in plugins:
        setup_plugin(plugin)

    return manager

def get_categories(plugin_manager):
    output = plugin_manager.getCategories()
    return output

def get_plugins_of_category(category_name, plugin_manager):
    output = plugin_manager.getPluginsOfCategory(category_name)    
    return output

def get_plugin_by_name(plugin_name, category_name, plugin_manager):
    output = plugin_manager.getPluginByName(plugin_name, category_name)
    return output

def get_plugin_info(plugin):
    categories = ", ".join([category for category in plugin.categories if category != "Plugin"])
    output = f"plugin: {plugin.name}\n" + \
            f"categories: {categories}\n" + \
            f"author: {plugin.author}\n" + \
            f"description: {plugin.description}."

    return output

def setup_plugin(plugin):
    plugin.plugin_object.setup(parent=plugin)

def run_plugin(plugin, sentence):
    plugin.plugin_object.run(sentence)

plugin_manager = setup_plugin_manager()

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
plugin = get_plugin_by_name("Gmail", "HandleEmail", plugin_manager)
run_plugin(plugin, "enviar email com título Olá e mensagem Oi Mundo")

# Explorer
# parei aqui.