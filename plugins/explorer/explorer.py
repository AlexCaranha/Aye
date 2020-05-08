from yapsy.IPlugin import IPlugin
from plugins.categories import HandleFile, Knowledge

class Explorer(HandleFile, Knowledge):
    def setup(self):
        print("setup done.")

    def run(self, input):
        return "done"
