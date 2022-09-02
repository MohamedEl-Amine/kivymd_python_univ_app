from kivy.uix.screenmanager import Screen


class InteractiveScreen(Screen):
    def clicked(self):
        print("clicked")
