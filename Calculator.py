import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window


Window.clearcolor = (1, 1, 1, 1)
char_set = {
    'e': f'{math.e}',
    'π': f'{math.pi}',
    '÷': '/',
    'x': '*',
    'm': '%',
    '^': "**"
}


class MyLayout(Widget):
    def button_symbol(self, instance):
        self.data.text += instance

    def clear(self):
        self.data.text = ""

    def delete(self):
        text = self.data.text
        self.data.text = text[0: len(text) - 1]

    def result(self):
        try:
            question = self.data.text
            new_question = ''
            for index in range(len(question)):
                new_question += char_set.get(question[index], question[index])
            answer = str(eval(new_question))
            self.data.text = answer
        except SyntaxError:
            self.data.text = "Syntax Error!!"
        except ZeroDivisionError:
            self.data.text = "Math Error!!"
        except:
            self.data.text = "Error!!"

    def absolute_value(self):
        try:
            question = self.data.text
            new_question = char_set.get(question, question)
            answer = str(eval(new_question))
            self.data.text = answer.replace('-', '')
        except SyntaxError:
            self.data.text = "Syntax Error!!"
        except:
            self.data.text = "Error!"

    def plusminus(self):
        try:
            question = self.data.text
            new_question = char_set.get(question, question)
            if '-' in new_question:
                self.data.text = new_question.replace('-', '')
            else:
                self.data.text = f'-{new_question}'
        except SyntaxError:
            self.data.text = "Syntax Error!!"
        except:
            self.data.text = "Error!!"

    def factorial(self):
        try:
            answer = 1
            question = int(self.data.text)
            if question > 15:
                self.data.text = "Can't get factorial greater than 15"
            elif question < 0:
                self.data.text = "Math Error!!"
            elif question == 0:
                self.data.text = "1"
            else:
                while question >= 1:
                    answer = answer * question
                    question = question - 1
                self.data.text = str(answer)
        except SyntaxError:
            self.data.text = "Syntax Error!!"
        except:
            self.data.text = "Math Error!!"

    def square(self):
        try:
            question = self.data.text
            new_question = char_set.get(question, question)
            self.data.text = str(eval(f'{new_question}**2'))
        except SyntaxError:
            self.data.text = "Syntax Error!!"
        except:
            self.data.text = "Math Error!!"

    def cube(self):
        try:
            question = self.data.text
            new_question = char_set.get(question, question)
            self.data.text = str(eval(f'{new_question}**3'))
        except SyntaxError:
            self.data.text = "Syntax Error!!"
        except:
            self.data.text = "Math Error!!"

    def reciprocal(self):
        try:
            question = self.data.text
            new_question = float(char_set.get(question, question))
            self.data.text = str(eval(f'{1/new_question}'))
        except SyntaxError:
            self.data.text = "Syntax Error!!"
        except:
            self.data.text = "Error!!"

    def square_root(self):
        try:
            question = self.data.text
            new_question = float(char_set.get(question, question))
            self.data.text = str(new_question ** 0.5)
        except SyntaxError:
            self.data.text = "Syntax Error!!"
        except:
            self.data.text = "Error!!"

    def log(self):
        try:
            question = self.data.text
            new_question = float(char_set.get(question, question))
            self.data.text = str(math.log10(new_question))
        except SyntaxError:
            self.data.text = "Syntax Error!!"
        except:
            self.data.text = "Error!"

    def ln(self):
        try:
            question = self.data.text
            new_question = float(char_set.get(question, question))
            self.data.text = str(math.log(new_question, math.e))
        except SyntaxError:
            self.data.text = "Syntax Error!!"
        except:
            self.data.text = "Error!"

    def power10(self):
        try:
            question = self.data.text
            new_question = float(char_set.get(question, question))
            self.data.text = str(eval(f'10**{new_question}'))
        except SyntaxError:
            self.data.text = "Syntax Error!!"
        except:
            self.data.text = "Error!!"

    def exponential(self):
        try:
            question = self.data.text
            new_question = float(char_set.get(question, question))
            self.data.text = str(eval(f'{math.e}**{new_question}'))
        except SyntaxError:
            self.data.text = "Syntax Error!!"
        except:
            self.data.text = "Error!!"


class CalcApp(App):
    def build(self):
        self.title = "7XCalculator"
        return MyLayout()


if __name__ == '__main__':
    CalcApp().run()
