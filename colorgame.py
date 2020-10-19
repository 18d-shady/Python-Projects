import tkinter as tk
import random

#list of possible colour.
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

# the game time left, initially 30 seconds
timeleft = 30

#function that willl start the game
def startGame(event):
    if timeleft == 30:
        
        #start the countdown timer
        countdown()
        
    #run the function to
    #choose next colour
    nextColour()

#function to choose and
#display the next colour
def nextColour():

    #use the globally declared score
    #and play  variables above
    global score
    global timeleft

    if timeleft > 0:

        #make the next entry box active
        e.focus_set()

        #if the colour typed is equal
        #to the colour of the text
        if e.get().lower() == colours[1].lower():

            score += 1


        #clear the text entry box
        e.delete(0, tk.END)

        random.shuffle(colours)

        #change the colour to type, by changing the
        #text _and_ the colour to a random colour value
        label.config(fg = str(colours[1]), text = str(colours[0]))

        #update the score
        scoreLabel.config(text = "Score: " + str(score))

#countdown timer function
def countdown():

    global timeleft

    #if a game is in play
    if timeleft > 0:

        #decrement the timer
        timeleft -= 1

        #update the time left label
        timeLabel.config(text = 'Time left: '
                         + str(timeleft))

        #run the function again after 1 second
        timeLabel.after(1000, countdown)


#Driver code

#create a GUI window
root = tk.Tk()

#set the title
root.title("COLORGAME")

#set the size
root.geometry("375x200")

#add an instructions label
instructions = tk.Label(root, text = "Type in the colour"
                        "of the words, and not the word text!",
                        font = ('Helvetica', 12))
instructions.pack()

#add a score label
scoreLabel = tk.Label(root, text = "Press enter to start",
                      font = ('Helvetica', 12))
scoreLabel.pack()

#add a time left label
timeLabel = tk.Label(root, text = "Time left: " +
                      str(timeleft), font = ('Helvetica', 12))
timeLabel.pack()

#add a label for displaying the colours
label = tk.Label(root, font = ('Helvetica', 60))
label.pack()

#add a text entry box for
#typing in colours
e = tk.Entry(root)

#run the 'startGame' function
#when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()

#set the focus on the entry box
e.focus_set()
            
#start the GUI
root.mainloop()
