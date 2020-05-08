
from plugins.categories import HandleFile, Knowledge, get_classes_categories
from yapsy.PluginManager import PluginManager

def setup_plugin_manager():    
    manager = PluginManager()
    manager.setCategoriesFilter(get_classes_categories())
    manager.setPluginPlaces(["plugins"])
    manager.collectPlugins()
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
            f"categorias: {categories}\n" + \
            f"autor: {plugin.author}\n" + \
            f"descrição: {plugin.description}."

    return output

plugin_manager = setup_plugin_manager()
print("Plugin: wikipedia\n")

category = "Knowledge"
plugin = get_plugin_by_name("Wikipedia", category, plugin_manager)
info = get_plugin_info(plugin)
print(info)

