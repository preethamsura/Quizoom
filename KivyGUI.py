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
from record import *
from Convert import *
import threading
    

filename = "Audio"


class WelcomeScreen(Screen):
    bg_color = ObjectProperty([145/255,183/255,250/255,1])

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        Clock.schedule_once(self.start_pulsing, 8)

    def start_pulsing(self, *args):
        anim = Animation(bg_color=[145/255,183/255,250/255,1]) + Animation(bg_color=[176/255,145/255,250/255,1])
        anim.repeat = True
        anim.start(self)

    """def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        self.add_widget(Label(text='Quizoom', font_size='30sp'))
        startButton = Button(text='Start')
        startButton.bind(on_press=startButtonClicked)
        self.add_widget(startButton)"""
        


class RecordScreen(Screen):
    bg_color = ObjectProperty([145/255,183/255,250/255,1])

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.recorded = False
        Clock.schedule_once(self.start_pulsing, 8)

    def start_pulsing(self, *args):
        anim = Animation(bg_color=[145/255,183/255,250/255,1]) + Animation(bg_color=[176/255,145/255,250/255,1])
        anim.repeat = True
        anim.start(self)

    """def __init__(self, **kwargs):
        super(RecordScreen, self).__init__(**kwargs)"""
    

    def onClick(self):
        if self.recorded:
            print("We have already recorded. Press next to see your questions.")
            return
        
        # Indicate that we have recorded
        self.recorded = True
        print("Audio Recording Started")

        # Set runDuration to the value in the text box
        self.runDuration = int(self.ids.reclength.text)
        self.remove_widget(self.ids.reclength)
        self.remove_widget(self.ids.back)

        # Duration of recording
        self.duration = 10

        # Creates all the threads which will run during this program
        self.threads = []
        for i in range(int(self.runDuration / self.duration) + 1):
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

class QuizScreen(Screen):
    bg_color = ObjectProperty([145/255,183/255,250/255,1])

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        Clock.schedule_once(self.start_pulsing, 8)
        self.questions = ['test']
        self.answers = ['test']
        self.current = 0
        self.max = 0
        #self.inputAnswer()

    def start_pulsing(self, *args):
        anim = Animation(bg_color=[145/255,183/255,250/255,1]) + Animation(bg_color=[176/255,145/255,250/255,1])
        anim.repeat = True
        anim.start(self)
        
    def nextQ(self):
        if self.current != self.max - 1:
             self.current += 1

    def prevQ(self):
        if self.current != 0:
            self.current -= 1

    def inputAnswer(self):
        readFile = "./TextFiles/Questionsrandom.txt"
        file1 = open(readFile, "r")
        self.max = int(file1.readline())
        
        for i in range(self.max):
            if (i == 0):
                self.questions[0] = file1.readline()
                self.answers[0] = file1.readline()
            else:
                self.questions.append(file1.readline())
                self.answers.append(file1.readline())
            file1.readline()
    pass

class WindowManager(ScreenManager):
    pass
