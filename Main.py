import kivy
from kivy.app import App
from kivy.lang import Builder
from KivyGUI import WelcomeScreen

kv = Builder.load_file("app.kv")

class MyApp(App):
    
    def build(self):
        return kv

if __name__ == '__main__':
    MyApp().run()