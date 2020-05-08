from yapsy.IPlugin import IPlugin
from plugins.categories import HandleFile
from googletrans import Translator

class Translate(HandleFile):
    def setup(self):
        translator = Translator()

    def translate_from_to(self, sentence, language_from, language_to):
        output = translator.translate(sentence, src=language_from, dest=language_to)
        return output['text']

    def translate_from_pt_to_en(self, sentence):
        output = translate_from_to(self, sentence, language_from="pt", language_to="en")
        return output

    def translate_from_en_to_pt(self, sentence):
        output = translate_from_to(self, sentence, language_from="en", language_to="pt")
        return output

    def run(self, input):
        return wiki.search(input)
