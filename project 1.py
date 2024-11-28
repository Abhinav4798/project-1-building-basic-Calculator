from tkinter import *
import math

# Initialize the main window
root = Tk()
root.title("Scientific Calculator")
root.resizable(width=False, height=False)
root.geometry("500x600")

# Create frames
cover_frame = Frame(root, bd=20, pady=2, relief=RIDGE)
cover_frame.grid()

cover_main_frame = Frame(cover_frame, bd=10, pady=2, bg='cadetblue', relief=RIDGE)
cover_main_frame.grid()

main_frame = Frame(cover_main_frame, bd=5, pady=2, relief=RIDGE)
main_frame.grid()


class Calculator:
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def number_enter(self, num):
        self.result = False
        first_num = ent_display.get()
        second_num = str(num)
        if self.input_value:
            self.current = second_num
            self.input_value = False
        else:
            if second_num == "." and "." in first_num:
                return
            self.current = first_num + second_num
        self.display(self.current)

    def display(self, value):
        ent_display.delete(0, END)
        ent_display.insert(0, value)

    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = self.current
        self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        elif self.op == "sub":
            self.total -= self.current
        elif self.op == "multi":
            self.total *= self.current
        elif self.op == "divide":
            self.total /= self.current
            
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def sum_total(self):
        self.result = True
        self.current = float(self.current)
        self.valid_function()

    def backspace(self):
        num_len = len(ent_display.get())
        ent_display.delete(num_len - 1, END)
        if num_len == 1:
            ent_display.insert(0, "0")

    def maths_pm(self):
        self.result = False
        self.current = -(float(ent_display.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(ent_display.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(ent_display.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(ent_display.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(ent_display.get())))
        self.display(self.current)


# Calculator object
calc = Calculator()

# Entry widget
ent_display = Entry(main_frame, font=('arial', 18, 'bold'), bd=14, width=22, bg='cadetblue', justify=RIGHT)
ent_display.grid(row=0, column=0, columnspan=4, pady=1)
ent_display.insert(0, "0")

# Buttons layout
buttons = [
    "C", "CE", "⌫", "±",
    "√", "cos", "tan", "sin",
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", ".", "=", "÷",
]

row = 1
col = 0

for button in buttons:
    if button in "0123456789.":
        cmd = lambda x=button: calc.number_enter(x)
    elif button == "C":
        cmd = calc.clear_entry
    elif button == "CE":
        cmd = calc.all_clear_entry
    elif button == "⌫":
        cmd = calc.backspace
    elif button == "±":
        cmd = calc.maths_pm
    elif button == "=":
        cmd = calc.sum_total
    elif button == "+":
        cmd = lambda x="add": calc.operation(x)
    elif button == "-":
        cmd = lambda x="sub": calc.operation(x)
    elif button == "*":
        cmd = lambda x="multi": calc.operation(x)
    elif button == "÷":
        cmd = lambda x="divide": calc.operation(x)
    elif button == "√":
        cmd = calc.squared
    elif button == "cos":
        cmd = calc.cos
    elif button == "tan":
        cmd = calc.tan
    elif button == "sin":
        cmd = calc.sin

    Button(main_frame, text=button, width=6, height=2, font=('arial', 16, 'bold'), bd=4, bg='cadetblue',
           command=cmd).grid(row=row, column=col, pady=1)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main loop
root.mainloop()
