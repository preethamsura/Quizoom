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
    # Record the audio for duration time and save it into filename.wav 
    fs = 44100
    myarray = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    wavio.write(filename + '.wav', myarray, fs, sampwidth=2)  
    #data = myarray 
    #scaled = np.int16(data/np.max(np.abs(data)) * 32767)

    # Convert the audio into a .flac file
    wav, samplerate = sf.read(filename+'.wav') 
    sf.write('test.flac', wav, samplerate)