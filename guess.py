dec = int(input("Guess a number: "))
dice = list(range(100))
def compare(a, b):
    if(a == 0) or (b == 0):
        pass
    elif(a == b):
        print("you got it right")
    elif(a > b):
            print("sorry, too high")
    elif(a < b):
            print("sorry, too low")

while(True):
    try:
        import random
        d = random.choice(dice)
        compare(dec, d)
            
    except():
        pass         
     
    try:
        dec = input("Guess again: ")
        if "no" in dec.lower():
            print("Hope you like it? \n Exiting......")
            break
        else:
            if dec.isdigit() == True:
                dec = int(dec)
            else:
                dec = 0
                raise TypeError
    except(TypeError):
        print("Error: ", str(TypeError))
        #break
