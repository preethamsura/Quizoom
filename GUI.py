# Using this to create the GUI
from tkinter import *
from tkinter.ttk import * 
from record import *
from Convert import *
import threading

class GUI():
    def __init__(self):
        # Window dimensions
        self.windowWidth = 600
        self.windowHeight = 500

        # Flac file to be converted to text
        self.filename = "Audio"

        # Time to run the whole simulation
        self.runDuration = 20

        # Duration of recording
        self.duration = 10

        # Creates all the threads which will run during this program
        self.threads = []
        for i in range(int(self.runDuration / self.duration) + 1):
            newFilename = self.filename + str(i)
            IBMThread = threading.Thread(target = convertIBM, args = (None, newFilename))
            recordThread = threading.Thread(target = record, args = (self.duration, newFilename, IBMThread, self.threads, i))
            self.threads.append(recordThread)

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

        # Runs the screen 
        gui.mainloop()

    # Action to perform when the button is clicked
    def recordAudio(self):
        # Starts the recording
        self.threads[0].start()