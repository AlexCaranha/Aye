
from sys import byteorder
import collections

import pyaudio
import audioop
import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 200

m = sr.Microphone()

def is_silence_in_buffer(buffer, source):
    energy = audioop.rms(buffer, source.SAMPLE_WIDTH)    
    output = energy < (r.energy_threshold * 1.5)

    return output

def is_above_of_threshold_in_seconds(
    qtd_buffer, buffer_samples,
    sample_rate, threshold_in_seconds=1.5):

    samples = qtd_buffer * buffer_samples
    seconds =  samples / sample_rate
    return seconds >= threshold_in_seconds

def listen_from_microphone():
    error = None
    try:
        with m as source:
            audio = listen_from_source(source)

            try:
                message = r.recognize_google(audio, language="pt-BR")

            except IndexError: # the API key didn't work
                message = None
                error = "No internet connection"

            except LookupError: # speech is unintelligible
                message = None
                error = "Could not understand audio"

            except sr.UnknownValueError:
                message = None
                error = "Comando não reconhecido."

            except sr.RequestError as e:
                message = None
                error = f"Não foi possível realizar requisição ao serviço de reconhecimento de fala da Google: {e}"

    except KeyboardInterrupt:
        error = "Interrupt by user."
        pass

    return (message, error)


def listen_from_source(source):

    p = pyaudio.PyAudio()
    stream = p.open(
        format=source.format, channels=1, rate=source.SAMPLE_RATE,
        input=True, output=True, frames_per_buffer=source.CHUNK)

    qtd_buffer_with_no_silence = 0
    qtd_buffer_with_silence = 0

    frames = collections.deque()
    r.listen

    is_command_started = False

    while True:
        buffer = source.stream.read(source.CHUNK)
        
        if len(buffer) == 0: break

        is_silence = is_silence_in_buffer(buffer, source)

        if is_silence:
            # if silence and command not started
            if not is_command_started:
                continue            

            # if silence and command already started 
            qtd_buffer_with_silence = 1 if qtd_buffer_with_silence == 0 else qtd_buffer_with_silence + 1
            
        elif not is_silence and not is_command_started:
            is_command_started = True
        
        frames.append(buffer)

        condition_to_stop_by_silence = is_above_of_threshold_in_seconds(qtd_buffer_with_silence, source.CHUNK, source.SAMPLE_RATE)
        if condition_to_stop_by_silence:
            break

    frame_data = b"".join(frames)
    return sr.AudioData(frame_data, source.SAMPLE_RATE, source.SAMPLE_WIDTH)


def adjust_threshold():
    """
    Adjust threshold to identify user's commands.
    """
    with m as source:
        r.adjust_for_ambient_noise(source, duration=0.5)

    print(f"energy threshold: {r.energy_threshold}")
