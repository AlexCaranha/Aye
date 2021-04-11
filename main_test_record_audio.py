
import audioop
import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

def adjust_threshold():
    with m as source:
        r.adjust_for_ambient_noise(source, duration=0.5)

    r.dynamic_energy_threshold = True  
    print(f"energy threshold: {r.energy_threshold}")
    return r.energy_threshold


from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave

THRESHOLD = adjust_threshold()
CHUNK_SIZE = m.CHUNK
FORMAT = m.format
RATE = m.SAMPLE_RATE

def is_silent(snd_data):    
    energy = audioop.rms(snd_data, m.SAMPLE_WIDTH)
    output = energy <= (THRESHOLD * 4)

    print(f"is silence? {output}, threshold = {THRESHOLD:0.2f}, energy = {energy:0.2f}")

    return output

def record():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True, frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    signal_started = False

    r = array('h')

    while True:
        buffer = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            buffer.byteswap()        

        silent = is_silent(buffer)

        if silent and signal_started:
            num_silent += 1
        elif not silent and not signal_started:
            signal_started = True

        if signal_started:
            r.extend(buffer)

            if num_silent > 50:
                break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    return (sample_width, r)

def record_to_file(path):
    "Records from the microphone and outputs the resulting data to 'path'"
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()

if __name__ == '__main__':
    print("please speak a word into the microphone")
    record_to_file('demo.wav')
    print("done - result written to demo.wav")