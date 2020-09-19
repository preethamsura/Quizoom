# Using this to create the GUI
from tkinter import *
from tkinter.ttk import * 
from record import *
from Convert import *
import threading
from GenerateQuestions import *

class GUI():
    def __init__(self):
        # Window dimensions
        self.windowWidth = 600
        self.windowHeight = 500

        # Flac file to be converted to text
        self.filename = "airplane"

        # Duration of recording
        self.duration = 1
        
        # Starts the application
        self.runGUI()

    # Starts the GUI
    def runGUI(self):
        # Create the screen
        gui = Tk()
        gui.title("Quizzoom")
        gui.minsize(self.windowWidth, self.windowHeight)

        # Generate the button style
        style = Style()
        style.configure('TButton', font = ('calibri', 30, 'bold', 'underline'), foreground = 'black') 

        # Creates the recording button
        recordButton = Button(gui, text = "Record Audio", style = 'TButton', command = self.recordAudio)
        recordButton.pack()

        # Button to playback recording
        playbackButton = Button(gui, text = "Playback Audio", style = 'TButton', command = self.playbackAudio)
        playbackButton.pack()

        # Convert wav to flac
        flacConvertButton = Button(gui, text = "Convert wav to flac", style = 'TButton', command = self.runflacConvert)
        flacConvertButton.pack()

        # Create the button which converts the audio from speech to text
        flacToTextButton = Button(gui, text = "Flac to Text", style = 'TButton', command = self.runIBMconvert)
        flacToTextButton.pack()

        # Runs convert to string
        stsButton = Button(gui, text = "String to Sentences", style = 'TButton', command = self.convertStringToSentences)
        stsButton.pack()
        
        # Take the sentences and call GenerateQuestions
        gqButton = Button(gui, text = "Make Questions", style = 'TButton', command = self.makeQuestions)
        gqButton.pack()

        # Creates a text input box
        # self.text = StringVar()
        # textEntered = Entry(gui, width = 15, textvariable = self.text)
        # textEntered.pack()

        # Runs the screen 
        gui.mainloop()

    # Action to perform when the button is clicked
    def recordAudio(self):
        # Starts the recording
        self.myarray = record(self.duration, self.filename)


    # Playback the audio which was previously recorded
    # Can only play audio after clicking record
    def playbackAudio(self):
        playback(self.myarray)


    # Converts a specified audio file into its text form.
    # File must be of form .flac for this to run
    def runIBMconvert(self):
        convertIBM(self.filename)


    # Takes in an input text file and rewrites it to have different sentences.
    def convertStringToSentences(self):
        convertSTS(self.filename)


    # Converts a wav file to a flac file. 
    def runflacConvert(self):
        wavToFlac(self.filename)


    # Creates question and answer pairs
    def makeQuestions(self):
        generateQuestions(self.filename)