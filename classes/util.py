# pip3 install screeninfo
# pip3 install pyuserinput
# pip3 install clipboard
# pip3 install pyhooked

# import pymouse
# from screeninfo import get_monitors
from playsound import playsound
import simpleaudio as sa

import os, sys
import os.path

from gtts import gTTS
from pydub import AudioSegment as am
__author__ = 'Alex Libório Caranha'

def resample(filepath: str, new_frame_rate: int = 8000):
    if not os.path.isfile(filepath):
        return False

    sound = am.from_file(filepath, format='wav')
    sound = sound.set_frame_rate(new_frame_rate)
    sound.export("output_8khz", format='wav')
    
    return True

# resample(".\input.wav")

def text_to_speech(text, vocoder_plugin, language="pt"):
    speech = gTTS(text = text, lang = language, slow = False)

    if vocoder_plugin == None:
        __gtts_to_wav__(speech, "output.wav")

    else:
        (status, error) = __gtts_to_wav__(speech, "output_temp.wav")

        if status == True and error is None:
            vocoder_plugin.plugin_object.change_time("output_temp.wav", "output.wav")
            delete_file("output_temp.wav")

    play_output()


def text_to_mp3(text, vocode_plugin, language="pt", mp3_filename):
    speech = gTTS(text = text, lang = language)

    if vocoder_plugin == None:
        __gtts_to_mp3__(speech, mp3_filename)

    else:
        (status, error) = __gtts_to_wav__(speech, "output_temp.wav")

        if status == True and error is None:
            vocoder_plugin.plugin_object.change_time("output_temp.wav", "output.wav")
            delete_file("output_temp.wav")
            convert_wav_to_mp3("output.wav", "output.mp3")


def __gtts_to_mp3__(speech, output_file):
    try:
        input_file = "output.wav"
        speech.save(input_file)

        convert_wav_to_mp3(input_file, output_file)
        delete_file(input_file)

    except:
        return (False, sys.exc_info()[0])

    return (True, None)


def __gtts_to_wav__(speech, output_file):
    try:
        input_file = "output.mp3"        
        speech.save(input_file)

        convert_mp3_to_wav(input_file, output_file)
        delete_file(input_file)

    except:
        return (False, sys.exc_info()[0])

    return (True, None)

def play_output():
    filename = 'output.wav'

    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing

    # playsound('output.wav')
    os.remove('output.wav')

def play(wavfile):
    playsound(wavfile)

def delete_file(file_name):
    os.remove(file_name)

def convert_mp3_to_wav(input_mp3: str, output_wav: str):
    sound = am.from_mp3(input_mp3)
    sound.export(output_wav, format="wav")

def convert_wav_to_mp3(input_wav: str, output_mp3: str):
    sound = am.from_wav(input_wav)
    sound.export(output_mp3, format="mp3")

def text_to_mp3(text: str, mp3_file_name: str)


# def get_center_of_current_monitor():
#     mouse = pymouse.PyMouse()
#     mouse_x, mouse_y = mouse.position()

#     # print("mouse.x: {0}, mouse.y: {1}".format(mouse_x, mouse_y))

#     monitors = get_monitors()

#     for iMonitor in range(0, len(monitors)):
#         monitor = monitors[iMonitor]

#         monitor_left = monitor.x
#         monitor_right = monitor.x + monitor.width
#         monitor_bottom = monitor.y
#         monitor_top = monitor.y + monitor.height

#         # print("monitor: {0}, width: {1}".format(iMonitor, monitor.width))
#         # print("left: {0}, right: {1}".format(monitor_left, monitor_right))

#         if monitor_left <= mouse_x < monitor_right and monitor_bottom <= monitor.y < monitor_top:
#             x = int((monitor_left + monitor_right)/2)
#             y = int((monitor.y + monitor.height)/2)
#             return x, y, monitor.width, monitor.height

#     return None, None, None, None
