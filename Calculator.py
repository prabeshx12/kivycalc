from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (0, 1, 0, 1)
Window.size = (350, 520)


class MyLayout(Widget):
    def clear(self):
        self.data.text = ''

    def button_press(self, button):
        prior = self.data.text
        self.data.text = f'{prior}{button}'

    def operator_sign(self, sign):
        prior = self.data.text
        self.data.text = f'{prior}{sign}'

    def point(self):
        prior = self.data.text
        self.data.text = f'{prior}.'

    def delete(self):
        prior = self.data.text
        new_data = prior[: -1]
        self.data.text = new_data

    def plusminus(self):
        prior = self.data.text
        if '-' in prior:
            self.data.text = f"{self.data.text.replace('-', '')}"
        else:
            self.data.text = f"-{prior}"

    def equal(self):
        prior = self.data.text
        try:
            answer = eval(prior)
            self.data.text = str(answer)

        except ZeroDivisionError:
            self.data.text = "Can't divide by zero"

        except:
            self.data.text = 'Error'

class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()
