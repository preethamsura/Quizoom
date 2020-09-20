import kivy
from kivy.app import App
from kivy.lang import Builder
from KivyGUI import WelcomeScreen
from KivyGUI import WindowManager
kv = Builder.load_file("app.kv")

class QuizoomApp(App):
    
    def build(self):
        return kv

# Creates the app as soon as we run this file
if __name__ == '__main__':
    QuizoomApp().run()