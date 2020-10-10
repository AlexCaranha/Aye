from yapsy.IPlugin import IPlugin
from plugins.categories import Entertainment
from fuzzywuzzy import fuzz
from pytube import YouTube
import re

class Youtube(Entertainment):
    def setup(self, parent):
        self.parent = parent
        self.__activate__(False)    

    def get_list_captions(self, url):
        source = YouTube(url)
        all = en_caption = source.captions.all()
        print(all)

    def __activate__(self, value):
        self.activated = value

    def run(self, input):
        print("nothing")