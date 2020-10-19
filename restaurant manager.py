from tkinter import*
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management Systems")

text_Input = StringVar
operator =""

Tops = Frame(root, width = 1600, height=50, bg="cyan", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800, height=700, bg="cyan", relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300, height=700, bg="cyan", relief=SUNKEN)
f2.pack(side=RIGHT)

#===================================Time================================
localtime=time.asctime(time.localtime(time.time()))

#=================================Info====================================================
lblInfo = Label(Tops, font=('arial',50, 'bold'), text= "Restaurant Management Systems", fg="Blue", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblInfo = Label(Tops, font=('arial',20, 'bold'), text= localtime, fg="Blue", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)

#=============================Calculator=======================
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
txtDisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="cyan", justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="7", bg="cyan", command=lambda: btnClick(7)).grid(row=2, column=0)

btn8=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="8", bg="cyan", command=lambda: btnClick(8)).grid(row=2, column=1)

btn9=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="9", bg="cyan", command=lambda: btnClick(9)).grid(row=2, column=2)

Addition=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="+", bg="cyan", command=lambda: btnClick('+')).grid(row=2, column=3)

btn4=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="4", bg="cyan", command=lambda: btnClick(4)).grid(row=3, column=0)

btn5=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="5", bg="cyan", command=lambda: btnClick(5)).grid(row=3, column=1)

btn6=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="6", bg="cyan", command=lambda: btnClick(6)).grid(row=3, column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="-", bg="cyan", command=lambda: btnClick('-')).grid(row=3, column=3)

btn1=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="1", bg="cyan", command=lambda: btnClick(1)).grid(row=4, column=0)

btn2=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="2", bg="cyan", command=lambda: btnClick(2)).grid(row=4, column=1)

btn3=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="3", bg="cyan", command=lambda: btnClick(3)).grid(row=4, column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="*", bg="cyan", command=lambda: btnClick('*')).grid(row=4, column=3)

btn0=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="0", bg="cyan", command=lambda: btnClick(0)).grid(row=5, column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="C", bg="cyan", command=btnClearDisplay).grid(row=5, column=1)

btnEquals=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="=", bg="cyan", command=btnEqualsInput).grid(row=5, column=2)

Division=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial',20,'bold'),
            text="/", bg="cyan", command=lambda: btnClick('/')).grid(row=5, column=3)









root.mainloop()
