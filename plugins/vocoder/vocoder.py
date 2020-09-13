from yapsy.IPlugin import IPlugin
from plugins.categories import Internal
from audiotsm import phasevocoder
from audiotsm.io.wav import WavReader, WavWriter
from fuzzywuzzy import fuzz
import re

class Vocoder(Internal):
    def setup(self, parent):
        self.parent = parent
        self.default_speed = 1.0
        self.speed = self.default_speed
        print(f"{parent.name} loaded: ok.")
            
    def is_the_question_with_sentence(self, pattern, input: str):
        match = re.search(pattern, input, re.IGNORECASE)
        return match.group('sentence') if match is not None else None

    def is_the_question(self, pattern, input: str):
        ratio = fuzz.token_set_ratio(pattern, input)
        return ratio > 85

    def is_activated_to_answer_now(self):
        return False

    def get_message_when_plugin_activated_to_answer_now(self):
        return None

    def change_time(self, input_file_name: str, output_file_name: str):       
        with WavReader(input_file_name) as reader:
            with WavWriter(output_file_name, reader.channels, reader.samplerate) as writer:
                tsm = phasevocoder(reader.channels, speed=self.speed)
                tsm.run(reader, writer)

    def run(self, input):
        if self.is_the_question(r'velocidade normal do áudio | normalizar áudio', input):
            self.speed = self.default_speed
            return f"velocidade do áudio normalizada."

        percentual = self.is_the_question_with_sentence(r'aumentar velocidade do áudio em (?P<sentence>.*)%', input)
        if percentual is not None:
            self.speed += (int(percentual) / 100)
            return f"velocidade do áudio aumentada em {self.percentual}%."

        percentual = self.is_the_question_with_sentence(r'diminuir velocidade do áudio em (?P<sentence>.*)%', input)
        if percentual is not None:
            self.speed -= (int(percentual) / 100)
            return f"velocidade do áudio reduzida em {self.percentual}%."

        return None