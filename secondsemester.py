from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class BoxInSecondSemester(GridLayout):
    name_modules = ["Electrotechnique appliquée", "Mécanique III", "Génie des proceeds II ", "Automatique II ",
                    "Architecture des ordinateurs", "Probabilités - Statistiques I ",
                    "Ordonnancement", "Planification", "Anglais II"]
    list_modules = {
        'GI411': [2, 3],
        'GI412': [2, 4],
        'GI413': [2, 4],
        'GI414': [2, 4],
        'GI415': [2, 3],
        'GI471': [2, 3],
        'GI472': [2, 4],
        'GI473': [2, 4],
        'GI401': [1, 1]
    }
    codes_modules = list(list_modules.keys())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.load_name_modules)
        self.add_widget(
            Label(text="[b][color=00666b]Calculate Semester 2 Result[/b][/color]", font_size=40, markup=True))

    def load_name_modules(self, dt):
        for i in range(len(self.name_modules)):
            idd = 'label = self.ids.text{}'.format(i)
            idd2 = 'label.text = self.codes_modules[{}]'.format(i)
            exec(idd)
            exec(idd2)

    def calculate(self):
        Control = []
        Exam = []
        erreur = False
        for i in range(len(self.list_modules)):
            for_cc = 'Control += [self.ids.cc{}.text]'.format(i)
            exec(for_cc)
            for_exam = 'Exam += [self.ids.exam{}.text]'.format(i)
            exec(for_exam)
            try:
                eval('float(self.ids.cc{}.text)'.format(i))
                eval('float(self.ids.exam{}.text)'.format(i))
            except:
                wrong = self.ids.WrongMessage
                wrong.text = 'Please check your typing'
                erreur = True
                break
            for f in Control:
                if float(f) > 20 or float(f) < 0:
                    wrong = self.ids.WrongMessage
                    wrong.text = 'Please check your typing'
                    erreur = True
                    break
            for g in Exam:
                if float(g) > 20 or float(g) < 0:
                    wrong = self.ids.WrongMessage
                    wrong.text = 'Please check your typing'
                    erreur = True
                    break

        if not erreur:
            result_text = StringProperty("AMINE")
            moyenne = []
            for i in range(len(self.list_modules)):
                moyenne += [(float(Control[i]) + float(Exam[i])) / 2]
            total = []
            for i in range(len(self.list_modules)):
                total += [moyenne[i] * self.list_modules[self.codes_modules[i]][0]]

            sum_total = sum(total)
            result = sum_total / 17
            result_text = "Your result is: " + str("%.2f" %result)
            print(result_text)
            wrong = self.ids.WrongMessage
            wrong.text = result_text


class SecondSemester(Screen):
    pass

# class BoxInSemester(GridLayout):
# def calculate(self):
# pass
