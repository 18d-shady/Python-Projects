import tkinter as tk
from tkinter import ttk
from datetime import date

class Cal():
    def __init__(self):
        #create a tkinter window
        self.root = tk.Tk()

        #add title
        self.root.title("Age Calculator")

        #make it unresizable
        self.root.resizable(False, False)
        self.widgets()

    #create widgets
    def widgets(self):
        #canvas = tk.Canvas(self.root, width = 300, height = 300)  
        #canvas.pack()  
        #img = tk.PhotoImage(file="davis.png")  
        #canvas.create_image(20, 20, anchor=NW, image=img)
        #create labels
        ttk.Label(self.root, text="Name:").grid(column=0, row=1, sticky='W')
        ttk.Label(self.root, text="Year:").grid(column=0, row=2, sticky='W')
        ttk.Label(self.root, text="Month:").grid(column=0, row=3, sticky='W')
        ttk.Label(self.root, text="Day:").grid(column=0, row=4, sticky='W')

        #create entrys
        self.name = tk.StringVar()
        self.name_entered = ttk.Entry(self.root, width=20, textvariable=self.name)
        self.name_entered.grid(column=1, row=1, padx = 50)

        self.year = tk.IntVar()
        self.year_entered = ttk.Entry(self.root, width=20, textvariable=self.year)
        self.year_entered.grid(column=1, row=2, padx = 50)

        self.month = tk.IntVar()
        self.month_entered = ttk.Entry(self.root, width=20, textvariable=self.month)
        self.month_entered.grid(column=1, row=3, padx = 50)

        self.day = tk.IntVar()
        self.day_entered = ttk.Entry(self.root, width=20, textvariable=self.day)
        self.day_entered.grid(column=1, row=4, padx = 50)

        self.calc = ttk.Button(self.root, text='Calculate Age', command=self.calculate)
        self.calc.grid(column=1, row=5, padx = 65)
        

    def calculate(self):
        nameu = self.name_entered.get()
        yearu = int(self.year_entered.get())
        monthu = int(self.month_entered.get())
        dayu = int(self.day_entered.get())
        today = date.today()
        age = nameu, 'is', today.year - yearu - ((today.month, today.day) <
                                    (monthu, dayu)), "years"
        #return age
        #creates a screen for the calculator
        #ttk.Label(self.root, text="Age:").grid(column=0, row=0, sticky='W')
        self.ss = tk.StringVar()
        screen = ttk.Entry(self.root, width=30, textvariable=self.ss)
        screen.grid(column=1, row=0, padx = 30)
        self.ss.set(age)
        
 

#allow it to run
cal = Cal()
cal.name_entered.focus()
cal.root.mainloop()
