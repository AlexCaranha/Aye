from yapsy.IPlugin import IPlugin
from plugins.categories import HandleFile, Knowledge

class Explorer(HandleFile, Knowledge):
    def setup(self, parent):
        self.parent = parent
        print(f"{parent.name} loaded: ok.")

    def run(self, input):
        return None
