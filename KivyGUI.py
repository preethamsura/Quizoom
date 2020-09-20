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
        Clock.schedule_once(self.start_pulsing, 8)

    def start_pulsing(self, *args):
        anim = Animation(bg_color=[145/255,183/255,250/255,1]) + Animation(bg_color=[176/255,145/255,250/255,1])
        anim.repeat = True
        anim.start(self)

    """def __init__(self, **kwargs):
        super(RecordScreen, self).__init__(**kwargs)"""
    def onClick(self):
        #link to record method

        print("Recording Started")
    pass

class QuizScreen(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        Clock.schedule_once(self.start_pulsing, 8)
        self.questions = []
        self.answers = []
        
    def inputAnswer(self):
        readFile = "./TextFiles/Questionsrandom.txt"
        file1 = open(readFile, "r")
        num = int(file1.readline())
        for i in range(num):
            self.questions.append(file1.readline())
            self.answers.append(file1.readline())
            file1.readline()
        


    def writeAnswers(self):
        pass

class WindowManager(ScreenManager):
    pass
