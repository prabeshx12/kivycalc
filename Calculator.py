from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (0, 1, 38/255, 1)
Window.size = (350, 500)


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
        # for addition
        if '+' in prior:
            self.data.text = ''
            numbers = prior.split('+')
            addition = 0
            for elements in numbers:
                addition += float(elements)
            self.data.text = str(addition)

            # for subtraction
        elif '-' in prior:
            self.data.text = ''
            numbers = prior.split('-')
            subtraction = 2 * float(str(numbers[0]))
            for elements in numbers:
                subtraction = subtraction - float(elements)
            self.data.text = str(subtraction)

            # for multiplication
        elif '*' in prior:
            self.data.text = ''
            numbers = prior.split('*')
            multiplication = 1
            for elements in numbers:
                multiplication = multiplication * float(elements)
            self.data.text = str(multiplication)

            # for division
        elif '/' in prior:
            self.data.text = ''
            numbers = prior.split('/')
            division = float(numbers[0]) / float(numbers[-1])
            self.data.text = str(division)

            # for percentage
        elif '%' in prior:
            self.data.text = ''
            self.data.text = str(int(prior[:-1])/100)


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()