from abc import ABC, abstractmethod

class PluginBase(ABC):
    @abstractmethod
    def get_category_description(self):
        return

    @abstractmethod
    def setup(self):
        return

    @abstractmethod
    def run(self, input):
        return

    @abstractmethod
    def is_activated_to_answer_now(self):
        return

    @abstractmethod
    def get_message_when_plugin_activated_to_answer_now(self):
        return
