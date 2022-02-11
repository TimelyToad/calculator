import tkinter as tk
root = tk.Tk()
root.geometry('325x500')
e = tk.Entry(root)
e.pack()
display_number = ''
class Button():
    def get_button(self):
        return tk.Button(self.window, text=self.text, command=self.output)
    def subtractioncheckequals(self):
        global display_number
        if '=' in str(display_number):
            if '-' in str(display_number):
                return True
                order = display_number.find('-')
                print(type(order))
                left_operand = display_number[0:int(order)]
                left_order = int(order) + 1
                right_operand = display_number[left_order:]
                righ_operand = right_operand[:-1]
                difference = minus(int(left_operand), int(righ_operand))
                display_number = difference
    def additioncheckequals(self):
        global display_number
        if '+' in display_number:
            if '=' in display_number:
                order = display_number.find('+')
                print(type(order))
                left_operand = display_number[0:int(order)]
                left_order = int(order) + 1
                right_operand = display_number[left_order:]
                righ_operand = right_operand[:-1]
                total = add(int(left_operand), int(righ_operand))
                display_number = total
                x = True

    def multiplicationcheckequals(self):
        global display_number
        if '=' in str(display_number):
            if 'x' in str(display_number):
                order = display_number.find('x')
                print(type(order))
                left_operand = display_number[0:int(order)]
                left_order = int(order) + 1
                right_operand = display_number[left_order:]
                righ_operand = right_operand[:-1]
                product = multiplication(int(left_operand), int(righ_operand))
                display_number = product

    def exponentcheckequals(self):
        print('yes')
        global display_number
        if '=' in str(display_number):
            if '^' in str(display_number):
                order = display_number.find('^')
                print(type(order))
                left_operand = display_number[0:int(order)]
                left_order = int(order) + 1
                right_operand = display_number[left_order:]
                righ_operand = right_operand[:-1]
                result = exponentiate(int(left_operand), int(righ_operand))
                display_number = result

    def removecheckpress(self):
        global display_number
        if 'ce' in str(display_number):
            order = display_number.find('ce')
            print(type(order))
            display_number = remove(str(display_number))

    def output(self):
        global display_number
        display_number += self.text
        print(display_number)
        self.additioncheckequals()
        self.subtractioncheckequals()
        self.multiplicationcheckequals()
        self.exponentcheckequals()
        self.removecheckpress()
        mylabel = tk.Label(root, text=display_number)
        mylabel.pack()

    def __init__(self, text, window):
        self.text=text
        self.window=window
        self.retrieve=self.get_button()
        self.retrieve.pack()

 #       def get_button(self):
 #           return tk.Button(self.window, text=self.text, command=self.output)


button0 = Button(text='0', window=root)
button1 = Button(text='1', window=root)
button2 = Button(text='2', window=root)
button3 = Button(text='3', window=root)
button4 = Button(text='4', window=root)
button5 = Button(text='5', window=root)
button6 = Button(text='6', window=root)
button7 = Button(text='7', window=root)
button8 = Button(text='8', window=root)
button9 = Button(text='9', window=root)
button_minus = Button(text='-', window=root)
button_times = Button(text='x', window=root)
button_divide = Button(text='/ ', window=root)
button_exponentiate = Button(text='^', window=root)
button_remove = Button(text='ce', window=root)
#button_remove = Button(text=)
button_equal = Button(text='=', window=root)
button_divide.retrieve.place(x=129, y=23)
button1.retrieve.place(x=25, y=23)
button2.retrieve.place(x=60, y=23)
button3.retrieve.place(x=95, y=23)
button4.retrieve.place(x=25, y=49)
button5.retrieve.place(x=60, y=49)
button6.retrieve.place(x=95, y=49)
button7.retrieve.place(x=25, y=75)
button8.retrieve.place(x=60, y=75)
button9.retrieve.place(x=95, y=75)
button_equal.retrieve.place(x=95, y=103)
button0.retrieve.place(x=60, y=103)
button_minus.retrieve.place(x=129, y=75)
button_times.retrieve.place(x=129, y=49)
button_plus = Button(text='+', window=root)
button_plus.retrieve.place(x=129, y=103)
button_exponentiate.retrieve.place(x=25, y=159)
button_remove.retrieve.place(x=25, y=103)
def add(a, b):
    return a+b
def minus(c, d):
    return c-d
def multiplication(e, f):
    return e*f
def division(g, h):
    return g/h
def exponentiate(i, j):
     return i**j
def remove(k):
    return k[:-3]
tk.mainloop()
