
from audiotsm import phasevocoder
from audiotsm.io.wav import WavReader, WavWriter
import classes.util as util

def change_time(input_file_name: str, output_file_name: str):
    with WavReader(input_file_name) as reader:
        with WavWriter(output_file_name, reader.channels, reader.samplerate) as writer:
            tsm = phasevocoder(reader.channels, speed=0.5)
            tsm.run(reader, writer)          

util.play("input.wav")
util.play("output_slow.wav")
util.play("output_fast.wav")
