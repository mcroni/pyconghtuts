from kivy.app import App
from kivy.uix.button import Button
from kivymd.theming import ThemeManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
import random
from kivy.animation import Animation
class Interface(BoxLayout):

    def __int__(self,**kwargs):
        super(Interface,self).__init__(**kwargs)

    def add(self):
        print("hi man")

        self.ids.second_button.text = str(random.randint(1,30))

    def move(self):
        anim = Animation(x=100,duration=.4)+Animation(x=0,duration=.2)
        anim.start(self)

        # Animation(x=100,y=10).start(self)
        #Animation(x=0).start(self)

class Test(App):
    title = "pycon app"
    theme_cls = ThemeManager()

    def build(self):
        global interface
        interface = Interface()
        return Interface()

    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__ == "__main__":
    Test().run()