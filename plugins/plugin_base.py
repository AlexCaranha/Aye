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
