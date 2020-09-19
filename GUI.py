# Using this to create the GUI
from tkinter import *
from tkinter.ttk import * 
from record import *
from IBM import *

# Starts the GUI
def runGUI():
    # Create the screen
    gui = Tk(className='Quizzoom')
    gui.geometry("500x500")

    # Generate the button style
    style = Style()
    style.configure('TButton', font = ('calibri', 30, 'bold', 'underline'), foreground = 'black') 

    # Creates the recording button
    button = Button(gui, text ="Record Audio", style = 'TButton', command = recordAudio)
    button.pack()

    # Create the button which converts the audio from speech to text
    button2 = Button(gui, text ="Convert Audio", style = 'TButton', command = runIBMconvert)
    button2.pack()

    # Runs the screen 
    gui.mainloop()

# Action to perform when the button is clicked
def recordAudio():
    record(5, "Test")

# Converts a specified audio file into its text form.
# File must be of form .flac for this to run
def runIBMconvert():
    txtToSpeech('audio-file')