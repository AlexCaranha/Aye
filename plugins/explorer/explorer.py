from yapsy.IPlugin import IPlugin
from plugins.categories import HandleFile, Knowledge

class Explorer(HandleFile, Knowledge):
    def setup(self, parent):
        self.parent = parent
        print(f"{parent.name} loaded: ok.")

    def is_activated_to_answer_now(self):
        return False

    def is_activated_to_answer_now(self):
        return False

    def get_message_when_plugin_activated_to_answer_now(self):
        return None

    def run(self, input):
        return None
