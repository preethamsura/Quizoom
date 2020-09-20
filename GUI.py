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
        self.filename = "random"

        # Duration of recording
        self.duration = 20
        
        # Create the thread for recording audio and converting it to a flac file.
        self.recordThread = threading.Thread(target = record, args = (self.duration, self.filename))
        self.recordNum = 0

        # Create IBMConvert thread
        self.IBMThread = threading.Thread(target = convertIBM, args = (None, self.filename))
        self.IBMNum = -1

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
        if (self.recordNum == -1):
            self.recordThread.start()
            self.recordNum += 1
        else:
            # If the first already is currently running, don't do anything 
            if (self.recordThread.is_alive()):
                print("Audio is already being recorded.")
            
            # If the thread stopped, create a new thread which will store a new wav file.
            else:
                self.recordThread.join()
                self.recordThread = threading.Thread(target = record, args = (self.duration, self.filename + str(self.recordNum)))
                self.recordThread.start()
                self.recordNum += 1

    # Converts a specified audio file into its text form.
    # File must be of form .flac for this to run
    def runIBMconvert(self):
        if (self.IBMNum >= self.recordNum):
            print("You do not have any recordings which need to be converted.")
        elif (self.IBMNum == -1):
            self.IBMThread.start()
            self.IBMNum += 1
        else:
            # If the first already is currently running, don't do anything 
            if (self.recordThread.is_alive()):
                print("Audio is already being recorded.")
            
            # If the thread stopped, create a new thread which will store a new wav file.
            else:
                self.IBMThread.join()
                self.IBMThread = threading.Thread(target = convertIBM, args = (self.filename + str(self.recordNum)))
                self.IBMThread.start()
                self.IBMNum += 1


    # Takes in an input text file and rewrites it to have different sentences.
    def convertStringToSentences(self):
        convertSTS(self.filename)


    # Creates question and answer pairs
    def makeQuestions(self):
        generateQuestions(self.filename)