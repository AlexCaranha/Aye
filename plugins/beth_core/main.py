
import pluggy

from classes.util import do_if, is_not_blank
from fuzzywuzzy import fuzz

import plugins.beth_core.module as module


hookimpl = pluggy.HookimplMarker('beth')

def get_class():
    return CorePlugin()

class CorePlugin:

    @hookimpl
    def setup(self):
        self.is_running = True

    @hookimpl
    def get_alias(self):
        return "core"

    @hookimpl
    def execute(self, input:str):

        # if is_the_question(r'que dia é hoje|qual dia é hoje|hoje é que dia|hoje é qual dia', input):
        #     return current_day()

        # if is_the_question(r'que horas são|agora é que horas|agora são que horas', input):
        #     return current_time()

        return None

    def is_magic_word_in_sentence(self, sentence:str):
        if sentence is None:
            return False

        sentence_lowered = sentence.lower()
        return "assistente" in sentence_lowered

    def listen(self):

        while True:
            (sentence, error) = module.listen_from_microphone()

            if self.is_magic_word_in_sentence(sentence):
                break

            # if error != None:
            #     break

        return (sentence, error)

    def adjust_threshold(self):
        module.adjust_threshold()

    def is_the_question(self, pattern, input: str, threshold = 85):
        ratio = fuzz.token_set_ratio(pattern, input)
        return ratio > threshold

    