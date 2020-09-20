# Using this to create the GUI
from tkinter import *
from tkinter.ttk import * 
from record import *
from Convert import *
import threading

class GUI():
    def __init__(self):
        # Window dimensions
        self.windowWidth = 200
        self.windowHeight = 200

        # Flac file to be converted to text
        self.filename = "Audio"

        # Time to run the whole simulation
        self.runDuration = 25

        # Duration of recording
        self.duration = 10
        
        # Create the thread for recording audio and converting it to a flac file.
        self.recordThread = threading.Thread(target = record, args = (self.duration, self.filename))
        self.recordNum = -1

        # Create IBMConvert thread
        self.IBMThread = threading.Thread(target = convertIBM, args = (None, self.filename))
        self.IBMNum = -1

        # Starts the application
        self.runGUI()

    # Starts the GUI
    def runGUI(self):
        # Create the screen
        gui = Tk()
        gui.title("Quizoom")
        gui.minsize(self.windowWidth, self.windowHeight)

        # Generate the button style
        style = Style()
        style.configure('TButton', font = ('calibri', 30, 'bold', 'underline'), foreground = 'black') 

        # Creates the recording button
        recordButton = Button(gui, text = "Record Audio", style = 'TButton', command = self.recordAudio)
        recordButton.pack()

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
            self.recordThread.join()
            self.runIBMconvert()
        
        # If it isn't the first time recording, previous thread will need to be stopped
        # New thread will need to be created
        else:
            # If the first already is currently running, don't do anything 
            if (self.recordThread.is_alive()):
                print("Audio is already being recorded.")
            
            # If the thread stopped, create a new thread which will store a new wav file.
            else:
                if (self.runDuration >= 0):
                    # If its not the first run through, do this
                    if (not (self.recordNum == 0)):
                        self.recordThread.join()
                        self.runDuration = self.runDuration - self.duration
                    
                    self.recordThread = threading.Thread(target = record, args = (self.duration, self.filename + str(self.recordNum)))
                    self.recordThread.start()
                    self.recordNum += 1
                    self.runIBMconvert()

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