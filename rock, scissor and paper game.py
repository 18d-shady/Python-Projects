#do the importing
import tkinter as tk
from tkinter import ttk
import random

#create a class
class Game():
    def __init__(self):
        #create an instance
        self.game = tk.Tk()

        # add a title
        self.game.title("Rock Paper and Scissor Game")

        #make it unresizable
        self.game.resizable(False, False)

        #creates the widgets
        self.create_widget()

    def create_widget(self):
        #add a button
        self.rock = ttk.Button(self.game, text="Rock", command=self.play1)
        self.rock.grid(column=0, row=0, padx=20)

        self.paper = ttk.Button(self.game, text="Paper", command=self.play2)
        self.paper.grid(column=0, row=1, padx=20)

        self.scissor = ttk.Button(self.game, text="Scissor", command=self.play3)
        self.scissor.grid(column=0, row=2, padx=20)

        ss = tk.StringVar()
        self.screen = ttk.Label(self.game, text="Your Score:0 \nComputer Score:0")
        self.screen.grid(column=0, row=3, sticky="W")

     
    #define the function for the widgets
    def play1(self):
        l = [self.rock, self.paper, self.scissor]
        comp = random.choice(l)
        if comp == self.rock:
            self.screen.configure(text="Your Choice: Rock \nComputer's Choice: Rock\nYour Score:0 \nComputer Score:0")

        elif comp == self.paper:
            self.screen.configure(text="Your Choice: Rock \nComputer's Choice: Paper\nYour Score:0 \nComputer Score:1")

        elif comp == self.scissor:
            self.screen.configure(text="Your Choice: Rock \nComputer's Choice: Scissor\nYour Score:1 \nComputer Score:0")

    def play2(self):
        l = [self.rock, self.paper, self.scissor]
        comp = random.choice(l)
        if comp == self.rock:
            self.screen.configure(text="Your Choice: Paper \nComputer's Choice: Rock\nYour Score:1 \nComputer Score:0")

        elif comp == self.paper:
            self.screen.configure(text="Your Choice: Paper \nComputer's Choice: Paper\nYour Score:0 \nComputer Score:0")

        elif comp == self.scissor:
            self.screen.configure(text="Your Choice: Paper \nComputer's Choice: Scissor\nYour Score:0 \nComputer Score:1")

    def play3(self):
        l = [self.rock, self.paper, self.scissor]
        comp = random.choice(l)
        if comp == self.rock:
            self.screen.configure(text="Your Choice: Scissor \nComputer's Choice: Rock\nYour Score:0 \nComputer Score:1")

        elif comp == self.paper:
            self.screen.configure(text="Your Choice: Scissor \nComputer's Choice: Paper\nYour Score:1 \nComputer Score:0")

        elif comp == self.scissor:
            self.screen.configure(text="Your Choice: Scissor \nComputer's Choice: Scissor\nYour Score:0 \nComputer Score:0")
        

        

        
        
        
#let it run
start = Game()
start.game.mainloop()
