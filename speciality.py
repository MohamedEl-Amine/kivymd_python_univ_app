from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class Speciality(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(
            Label(text="[b][color=00666b]genie productique - Tlemcen[/b][/color]", font_size=40, markup=True))
        self.add_widget(
            Label(text="[b][color=00666b]genie productique - Tlemcen[/b][/color]", font_size=40, markup=True))