# Records audio directly from the computer
import sounddevice as sd
import soundfile as sf
import wavio
# Initial recording is saved as a np file
import numpy as np
from scipy.io.wavfile import write

# Used to dictate how long we are recording for
import time

# Record audio for duration seconds
def record(duration, filename):
    print("Audio is being recorded")

    # Default Variables
    fs = 44100
    sd.default.samplerate = fs
    sd.default.channels = 2

    # Record the audio for duration time and save it into filename + ".wav" 
    myarray = sd.rec(int(duration * fs))
    sd.wait()
    wavio.write("./WavFiles/" + filename + '.wav', myarray, fs, sampwidth=2)
    
    print("Finished recording. File saved in " + filename + ".wav")

# Plays back an audio file once recorded
def playback(myarray):
    fs = 44100
    sd.play(myarray, fs)

# Converts a .wav file to .flac
def wavToFlac(filename):
    wav, samplerate = sf.read("./WavFiles/" + filename + '.wav')
    sf.write("./FlacFiles/" + filename + '.flac', wav, samplerate)