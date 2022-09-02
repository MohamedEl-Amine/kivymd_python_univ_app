from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.lang import Builder


Builder.load_file('surface.kv')
Builder.load_file('interactive.kv')
Builder.load_file('secondsemester.kv')
Builder.load_file('firstsemester.kv')
Builder.load_file('info.kv')
Builder.load_file('speciality.kv')





class WindowManager(ScreenManager):
    pass


class CalculApp(MDApp):
    def build(self):
        self.icon = "images/icon.png"

CalculApp().run()
