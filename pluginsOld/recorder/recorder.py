
from plugins.categories import HandleFile

class Recorder(HandleFile):
    def setup(self, parent):
        self.parent = parent
        self.activated = False
        print(f"{parent.name} loaded: ok.")

    def get_message_when_plugin_activated_to_answer_now(self):
        return None

    def is_activated_to_answer_now(self):
        return self.activated

    def run(self, input):
        if self.activated:
            if self.is_the_question(r'terminar gravação de áudio', input, 95):
                self.activated = False
                return "Gravação finalizada."
                
        
        if self.is_the_question(r'nova gravação de áudio', input, 95):
            self.activated = True
            return "Gravação iniciada."


# from pydub import AudioSegment

# sound1 = AudioSegment.from_wav("/path/to/file1.wav")
# sound2 = AudioSegment.from_wav("/path/to/file2.wav")

# combined_sounds = sound1 + sound2
# combined_sounds.export("/output/path.wav", format="wav")
