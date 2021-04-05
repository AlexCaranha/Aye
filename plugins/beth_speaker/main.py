
import pluggy
import pyttsx3
# from pyttsx3.drivers import sapi5
from plugins.beth_speaker.module import set_rate, is_the_question_with_sentence, is_the_question

hookimpl = pluggy.HookimplMarker('beth')

def get_class():
    return SpeakerPlugin()

class SpeakerPlugin:

    @hookimpl
    def setup(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.voices = [voice for voice in self.voices if "PT-BR" in voice.id]    
        self.default_rate = self.engine.getProperty('rate')
        self.rate = self.default_rate

    @hookimpl
    def get_alias(self):
        return "speak"

    @hookimpl
    def execute(self, input:str):

        if is_the_question(r'normalizar velocidade', input):
            set_rate(self.engine, self.default_rate)
            return f"velocidade do áudio normalizada."

        phrase = is_the_question_with_sentence(r'speak (?P<sentence>.*)', input)
        if phrase is not None:        
            self.speak_phrase(phrase)
            return None

        percentual = is_the_question_with_sentence(r'aumentar a velocidade em (?P<sentence>.*)%', input)
        if percentual is not None:
            set_rate(self.engine, None, +(int(percentual) / 100))
            return f"velocidade do áudio aumentada em {percentual}%."

        percentual = is_the_question_with_sentence(r'diminuir a velocidade em (?P<sentence>.*)%', input)
        if percentual is not None:
            set_rate(self.engine, None, -(int(percentual) / 100))
            return f"velocidade do áudio reduzida em {percentual}%."

        return None

    def speak_phrase(self, text):
        for voice in self.voices:
            self.engine.setProperty('voice', voice.id)
            self.engine.say(text)
            self.engine.runAndWait()
            self.engine.stop()
            break
