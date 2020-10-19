dec = input("Roll dice????, Y or n : ")
dice = list(range(1, 7))
while(True):
    if dec == 'y':
        import random
        d = random.choice(dice)
        print(d)
    elif dec == 'n':
        quit()
    try:
        if 'n' in input("Roll more? y or no: "):
            break
    except():
        pass
        
    
