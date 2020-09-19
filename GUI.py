# Using this to create the GUI
from tkinter import *
from tkinter.ttk import * 
from record import *

# Starts the GUI
def runGUI():
    # Create the screen
    gui = Tk(className='Quizzoom')
    gui.geometry("500x500")

    # Creates the button and adds it to the screen
    style = Style()
    style.configure('TButton', font = ('calibri', 30, 'bold', 'underline'), foreground = 'black') 
    button = Button(gui, text ="Record Audio", style = 'TButton', command = recordAudio)
    button.pack()

    # Runs the screen 
    gui.mainloop()

# Action to perform when the button is clicked
def recordAudio():
    record(5, "Test")
    