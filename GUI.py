# Using this to create the GUI
from tkinter import *
from tkinter.ttk import * 
from record import *
from IBM import *

class GUI():
    
    def __init__(self):
        # Change this to change the filename input
        self.flacFilename = "Ctf"

        self.wavFilename = "Test"

        # Starts the application
        self.runGUI()



    # Starts the GUI
    def runGUI(self):
        # Create the screen
        gui = Tk(className='Quizzoom')
        gui.geometry("500x500")

        # Generate the button style
        style = Style()
        style.configure('TButton', font = ('calibri', 30, 'bold', 'underline'), foreground = 'black') 

        # Creates the recording button
        recordButton = Button(gui, text = "Record Audio", style = 'TButton', command = self.recordAudio)
        recordButton.pack()

        playbackButton = Button(gui, text = "Playback Audio", style = 'TButton', command = self.playbackAudio)
        playbackButton.pack()

        flacConvertButton = Button(gui, text = "Convert wav to flac", style = 'TButton', command = self.runflacConvert)
        flacConvertButton.pack()

        # Create the button which converts the audio from speech to text
        flacToTextButton = Button(gui, text = "Flac to Text", style = 'TButton', command = self.runIBMconvert)
        flacToTextButton.pack()

        # Runs the screen 
        gui.mainloop()



    # Action to perform when the button is clicked
    def recordAudio(self):
        # Change this to change the duration of the recording
        duration = 1
        # Change this to change which file you are reading sound to
        filename = "TestRecord"

        # Starts the recording
        self.myarray = record(duration, filename)



    # Playback the audio which was previously recorded
    def playbackAudio(self):
        playback(self.myarray)



    # Converts a specified audio file into its text form.
    # File must be of form .flac for this to run
    def runIBMconvert(self):
        txtToSpeech(self.flacFilename)



    # Converts a wav file to a flac file. 
    def runflacConvert(self):
        wavToFlac(self.wavFilename)