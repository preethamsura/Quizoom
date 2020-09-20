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
def record(duration, filename, IBMthread, threadList, index):
    # Closes all the previous threads
    i = 1
    while(i < index):
        if (not threadList[i].is_alive()):
            threadList[i].join()
        i = i + 1

    # Indicate that audio is being recorded
    print("Audio" + str(index) + " is being recorded")

    # Default Variables
    fs = 44100
    sd.default.samplerate = fs
    sd.default.channels = 2

    # Record the audio for duration time and save it into filename + ".wav" 
    myarray = sd.rec(int(duration * fs))
    sd.wait()
    wavio.write("./WavFiles/" + filename + '.wav', myarray, fs, sampwidth=2)
    
    # Prints that this recording has finished
    print("Finished recording. File saved in " + filename + ".wav")

    # Converts the file to a flac
    wavToFlac(filename)

    # Starts converting the created flac to a text file
    IBMthread.start()

    # Starts the next recording
    if (index < len(threadList) - 1):
        threadList[i + 1].start()
    
    # Ends IBMthread
    IBMthread.join()
    threadList[0] = threadList[0] + 1

# Converts a .wav file to .flac
def wavToFlac(filename):
    print("Started convert " + filename + "wav to flac")

    # Reads the wav file and writes it into a flac
    wav, samplerate = sf.read("./WavFiles/" + filename + '.wav')
    sf.write("./FlacFiles/" + filename + '.flac', wav, samplerate)

    print("Finished converting " + filename + "wav to flac")