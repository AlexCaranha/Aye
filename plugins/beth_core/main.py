
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

    def listen(self, is_print:bool):
        phrase_time_limit = 3
        (phrase, error) = module.listen(phrase_time_limit)

        do_if(print(phrase), condition=(is_print and is_not_blank(phrase)))
        do_if(print(error), condition=(is_print and is_not_blank(error)))

        return (phrase, error)

    def adjust_threshold(self):
        module.adjust_threshold()

    def is_the_question(self, pattern, input: str, threshold = 85):
        ratio = fuzz.token_set_ratio(pattern, input)
        return ratio > threshold

    