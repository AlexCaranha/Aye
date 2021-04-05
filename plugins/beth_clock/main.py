
import pluggy
from datetime import date
from datetime import datetime
from fuzzywuzzy import fuzz

hookimpl = pluggy.HookimplMarker('beth')

def get_class():
    return ClockPlugin()

class ClockPlugin:

    @hookimpl
    def setup(self):
        pass

    @hookimpl
    def get_alias(self):
        return "clock"

    @hookimpl
    def execute(self, input:str):

        if self.is_the_question(r'que dia é hoje|qual dia é hoje|hoje é que dia|hoje é qual dia', input):
            return self.current_day()

        if self.is_the_question(r'que horas são|agora é que horas|agora são que horas', input):
            return self.current_time()

        return None

    def is_the_question(self, pattern, input: str, threshold = 85):
        ratio = fuzz.token_set_ratio(pattern, input)
        return ratio > threshold

    def current_day(self):
        meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
        today = date.today()
        return f"Hoje é dia {today.day} de {meses[today.month-1]} de {today.year}."

    def current_time(self):
        horas = ('zero', 'uma', 'duas', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte', 'vinte e uma', 'vinte e duas', 'vinte e três', 'vinte e quatro')
        now = datetime.now()
        
        output = f"Horário atual: {horas[now.hour]} horas e {now.minute} minutos."
        return output
