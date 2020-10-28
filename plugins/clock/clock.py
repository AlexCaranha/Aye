
from plugins.categories import Internal
from plugins.clock.module import current_day, current_time
from classes.util import is_the_question

class Clock(Internal):
    def setup(self):
        print(f"Clock loaded: ok.")

    def get_message_when_plugin_activated_to_answer_now(self):
        return ""

    def is_activated_to_answer_now(self):
        return ""

    def run(self, input):        
        if is_the_question(r'que dia é hoje|qual dia é hoje|hoje é que dia|hoje é qual dia', input):
            return current_day()

        if is_the_question(r'que horas são|agora é que horas|agora são que horas', input):
            return current_time()

        return None
