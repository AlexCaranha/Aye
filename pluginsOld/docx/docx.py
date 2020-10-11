from yapsy.IPlugin import IPlugin
from plugins.categories import HandleDocument
import classes.util as util
import re
import docx

class Docx(HandleDocument):
    def setup(self, parent):
        self.parent = parent        
        print(f"{parent.name} loaded: ok.")

    def is_activated_to_answer_now(self):
        return False

    def get_message_when_plugin_activated_to_answer_now(self):
        return None

    def docx_to_string(self, docx_filename: str):
        doc = docx.Document(docx_filename)
        fullText = []

        for para in doc.paragraphs:
            if (para.text != ""):
                fullText.append(para.text)

        return "\n".join(fullText)
 
    def docx_to_mp3(self, docx_filename: str, mp3_filename: str):
        text = docx_to_string(docx_filename)
        

    def is_the_question(self, pattern, input: str):
        match = re.search(pattern, input, re.IGNORECASE)
        return match        

    def run(self, input):
        return None
        # match = self.is_the_question(r'ler arquivo (?P<docx_filename>*.docx) e gravar áudio (?P<mp3_filename>.*.mp3)', input)
        # if match:
        #     docx_filename = match.group('docx_filename')
        #     mp3_filename = match.group('mp3_filename')

        #     self.docx_to_mp3(subject, message)
        #     return "e-mail enviado com sucesso."

        # # Ler e copiar para o clipboard.
        

        # # Gerar audio via clipboard.


        # match = self.is_the_question(r'enviar e-mail com o título (?P<subject>.*) e a mensagem (?P<message>.*)', input)
        # if match:
        #     subject = match.group('subject')
        #     message = match.group('message')

        #     self.send_mail(subject, message)
        #     return "e-mail enviado com sucesso."

text = docx_to_string("C:\\Temp\\teste.docx")
print(text)