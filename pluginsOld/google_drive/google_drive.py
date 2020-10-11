
from yapsy.IPlugin import IPlugin
from plugins.categories import HandleEmail

import re

class GoogleDrive(HandleEmail):
    def setup(self, parent):
        self.parent = parent        
        print(f"{parent.name} loaded: ok.")

    def is_the_question(self, pattern, input: str):
        match = re.search(pattern, input, re.IGNORECASE)
        return match

    def is_activated_to_answer_now(self):
        return False

    def get_message_when_plugin_activated_to_answer_now(self):
        return None

    def run(self, input):
        # Do nothing.
        return None
