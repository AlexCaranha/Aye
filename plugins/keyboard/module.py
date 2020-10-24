
import keyboard
from classes.util import is_blank


def write_sentence(sentence:str):
    if is_blank(sentence):
        return "texto não informado"

    formated = sentence.capitalize()
    if not formated.endswith("."):
        formated += "."

    keyboard.write(formated)
    return formated

def new_paragraph():
    keyboard.press_and_release('enter, enter')
    return "Enter pressionado duas vezes."

def select_all():
    keyboard.send('ctrl+a')
    return "Texto selecionado."

def go_to_start_position():
    keyboard.send('pageup+home')
    return "Texto selecionado."

def go_to_end_position():
    keyboard.send('pagedown+end')
    return "Texto selecionado."


# print(new_paragraph())
# print(select_all())
