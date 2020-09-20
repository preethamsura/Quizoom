# Kivy Imports
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.animation import Animation
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

# Other project imports
from record import *
from Convert import *
import threading
    
# Default filename which is going to be saved
filename = "Quizoom"
numFiles = 2

# Welcome screen. Click next to move to the actual application.
class WelcomeScreen(Screen):
    bg_color = ObjectProperty([145/255,183/255,250/255,1])

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        Clock.schedule_once(self.start_pulsing, 8)

    def start_pulsing(self, *args):
        anim = Animation(bg_color=[145/255,183/255,250/255,1]) + Animation(bg_color=[176/255,145/255,250/255,1])
        anim.repeat = True
        anim.start(self)
    pass

# Screen where you can record the audio. The user can input a select time to record audio.
class RecordScreen(Screen):
    bg_color = ObjectProperty([145/255,183/255,250/255,1])
    
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.recorded = False
        Clock.schedule_once(self.start_pulsing, 8)

    # Changing background colors
    def start_pulsing(self, *args):
        anim = Animation(bg_color=[145/255,183/255,250/255,1]) + Animation(bg_color=[176/255,145/255,250/255,1])
        anim.repeat = True
        anim.start(self)

    # Starts the audio recording upon clicking that button
    def onClick(self):
        global numFiles
        if self.recorded:
            print("We have already recorded. Press next to see your questions.")
            return
        
        # Indicate that we have recorded
        self.recorded = True
        print("Audio Recording Started")

        # Set runDuration to the value in the text box
        self.runDuration = int(self.ids.reclength.text) - 1

        # Duration of recording
        self.duration = 10

        # Creates all the threads which will run during this program
        self.threads = []
        numFiles = int(self.runDuration / self.duration) + 1
        for i in range(numFiles):
            # Adds the index to the filename. 
            newFilename = filename + str(i)

            # Thread which will convert the file from a .flac file to its text equivalent (Speech to Text)
            IBMThread = threading.Thread(target = convertIBM, args = (None, newFilename))

            # Thread which will record audio and convert it to text. It calls on the IBMThread to convert the recorded audio to text
            recordThread = threading.Thread(target = record, args = (self.duration, newFilename, IBMThread, self.threads, i))
            
            # Array which stores all the threads which will eventually be run
            self.threads.append(recordThread)
            
        # Starts the thread which records audio
        self.threads[0].start()
    pass

# Screen where converted questions
class QuizScreen(Screen):
    bg_color = ObjectProperty([145/255,183/255,250/255,1])

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        Clock.schedule_once(self.start_pulsing, 8)
        Clock.schedule_interval(self.update, 1)
        self.questions = []
        self.answers = []
        self.current = 0
        self.opac = .1
        self.text = ""
    
    def on_pre_enter(self):
        self.inputAnswer()

    def start_pulsing(self, *args):
        anim = Animation(bg_color=[145/255,183/255,250/255,1]) + Animation(bg_color=[176/255,145/255,250/255,1])
        anim.repeat = True
        anim.start(self)

    def update(self, *args):
        print(self.current)
        if (len(self.questions) == 0):
            self.text = ""
        else:
            self.text = self.questions[self.current]
        self.ids.question.text = self.text
        
    def nextQ(self):
        if self.current != len(self.questions) - 1:
            print("increment")
            self.current += 1

    def prevQ(self):
        if self.current != 0:
            self.current -= 1

    def inputAnswer(self):
        for j in range(numFiles):
            readFile = "./QuestionFiles/" + filename + str(j) + ".txt"
            file1 = open(readFile, "r") 
            maxN = int(file1.readline())
            self.opac = 0
            for i in range(maxN):
                self.questions.append(file1.readline())
                self.answers.append(file1.readline())
                file1.readline()
        print(self.questions)
    pass

class WindowManager(ScreenManager):
    pass
