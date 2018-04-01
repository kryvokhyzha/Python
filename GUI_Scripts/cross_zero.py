from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.config import Config

Config.set("graphics","resizable","0")
Config.set("graphics","width","300")
Config.set("graphics","height","300")

choice = ['X', 'O']
switch = 0

class MainApp(App):

    def cross_zero(self, arg):
        global switch

        arg.disabled = True
        arg.text = choice[switch]

        if not switch: switch = 1
        else: switch = 0

        vector_x = (
            [self.button[x].text for x in (0,1,2)],
            [self.button[x].text for x in (3,4,5)],
            [self.button[x].text for x in (6,7,8)]
        )

        vector_y = (
            [self.button[y].text for y in (0,3,6)],
            [self.button[y].text for y in (1,4,7)],
            [self.button[y].text for y in (2,5,8)]
        )
        
        vector_d = (
            [self.button[d].text for d in (0,4,8)],
            [self.button[d].text for d in (2,4,6)]
        )

        green = [0,1,0,1]
        win = False

        for index in range(3):
            if vector_x[index].count('X') == 3\
            or vector_x[index].count('O') == 3:
                win = True
                if index == 0:
                    for i in (0,1,2):
                        self.button[i].color = green
                elif index == 1:
                    for i in (3,4,5):
                        self.button[i].color = green
                elif index == 2:
                    for i in (6,7,8):
                        self.button[i].color = green
                break

        for index in range(3):
            if vector_y[index].count('X') == 3\
            or vector_y[index].count('O') == 3:
                win = True
                if index == 0:
                    for i in (0,3,6):
                        self.button[i].color = green
                elif index == 1:
                    for i in (1,4,7):
                        self.button[i].color = green
                elif index == 2:
                    for i in (2,5,8):
                        self.button[i].color = green
                break

        for index in range(2):
            if vector_d[index].count('X') == 3\
            or vector_d[index].count('O') == 3:
                win = True
                if index == 0:
                    for i in (0,4,8):
                        self.button[i].color = green
                elif index == 1:
                    for i in (2,4,6):
                        self.button[i].color = green
                break

        if win:
            for index in range(9):
                self.button[index].disabled = True
        
    def restart(self, arg):
        global switch; switch = 0
        for index in range(9):
            self.button[index].color = [0,0,0,1]
            self.button[index].text = ""
            self.button[index].disabled = False

    def build(self):
        self.title = "Крестики-нолики"
        
        root = BoxLayout(orientation = "vertical", padding = 5)

        grid = GridLayout(cols = 3)
        self.button = [0 for _ in range(9)]
        for index in range(9):
            self.button[index] = Button(
                    color = [0,0,0,1],
                    font_size = 24,
                    disabled = False,
                    on_press = self.cross_zero
                )
            grid.add_widget(self.button[index])
        root.add_widget(grid)

        root.add_widget(
            Button(
                text = "Restart",
                size_hint = [1,.1],
                on_press = self.restart
            )
        )
        return root

if __name__ == "__main__":
    MainApp().run()