import tkinter as tk
from tkinter import ttk

#creat an instance
cal = tk.Tk()

#title
cal.title("Calculator")

#create two entry box that takes in integers
label = ttk.Label(cal, text="Input a number:")
label.grid(column=0, row=1, sticky=tk.W)
digit = tk.IntVar()
digbox = ttk.Entry(cal, width=12, textvariable=digit)
digbox.grid(column=1, row=1, sticky=tk.W)

label2 = ttk.Label(cal, text="Input a second number:")
label2.grid(column=0, row=3, sticky=tk.W)
digit2 = tk.IntVar()
digbox2 = ttk.Entry(cal, width=12, textvariable=digit2)
digbox2.grid(column=1, row=3, sticky=tk.W)

#creates a box that takes in an operator
label3 = ttk.Label(cal, text="Select Operation")
label3.grid(column=0, row=2, sticky=tk.W)
operator = tk.StringVar()
choose_operator = ttk.Combobox(cal, width=6, textvariable=operator, state='readonly')
choose_operator['values'] = ('+', '-', '/', 'x')
choose_operator.grid(column=1, row=2, sticky=tk.W)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

res = 0
def cal_fnc():
    try:
        dig_get=int(digbox.get())
        oper_get=choose_operator.get()
        dig2_get=int(digbox2.get())
    
        if oper_get == '+':
            res = add(dig_get, dig2_get)
        
        elif oper_get == '-':
            res = subtract(dig_get, dig2_get)
        
    
        elif oper_get == 'x':
            res = multiply(dig_get, dig2_get)
        
        elif oper_get == '/':
            res = divide(dig_get, dig2_get)

        ss.set(res)

    except:
        res = ValueError
        ss.set(res)

    
    
        

#creates a button that allows the user to calculate
action = ttk.Button(cal, text="Calculate", command=cal_fnc)
action.grid(column=1, row=4)

#creates a screen for the calculator
ss = tk.StringVar()
screen = ttk.Entry(cal, width=30, textvariable=ss)
screen.grid(column=0, row=0)




cal.mainloop()
