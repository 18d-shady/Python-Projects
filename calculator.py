def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def multipleAddition(x, y, z):
    return x + y + z

def multipleSubtraction(x, y, z):
    return x - y - z

def multipleDivision(x, y, z):
    return x / y / z

def multipleMultiplication(x, y, z):
    return x * y * z

def printHelp():
    print("Select Operation.")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Add 3 numbers")
    print("6. Subtract 3 numbers")
    print("7. Multiply 3 numbers")
    print("8. Divide 3 numbers")

def getValues():
    l = []
    choice = input("Enter choice(1, 2, 3, 4, 5, 6, 7, 8): ")    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    l.append(choice)
    l.append(num1)
    l.append(num2)
    l.append(num3)
    return l

def calcualte(choice, num1, num2):
    """
    This funtion helps to calculate the
    addition/substarcyion/multiplication/divition
    of two numbers.
    
    """
    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))

    elif choice == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))

    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1,num2))

def calculate(choice, num1, num2, num3):
    if choice == '5':
        print(num1,"+",num2,"+",num3,"=", multipleAddition(num1,num2,num3))
        
    elif choice == '6':
        print(num1,"-",num2,"-",num3,"=", multipleSubtraction(num1,num2,num3))

    elif choice == '7':
        print(num1,"*",num2,"*",num3,"=", multipleMultiplication(num1,num2,num3))

    elif choice == '8':
        print(num1,"/",num2,"/",num3,"=", multipleDivision(num1,num2,num3))


def run():
    try:
        l = getValues()
##        print(l)
        choice = l[0]
        num1 = l[1]
        num2 = l[2]
        num3 = l[3]
        if choice == '1':
            calcualte(choice, num1, num2)
        elif choice == '2':
            calcualte(choice, num1, num2)
        elif choice == '3':
            calcualte(choice, num1, num2)
        elif choice == '4':
            calcualte(choice, num1, num2)
        elif choice == '5':
            calculate(choice, num1, num2, num3)
        elif choice == '6':
            calculate(choice, num1, num2, num3)
        elif choice == '7':
            calculate(choice, num1, num2, num3)
        elif choice == '8':
            calculate(choice, num1, num2, num3)
        
        
    except(ValueError):
             print("Error: ", ValueError)



        
def keepRunning():
    printHelp()
    while(True):
        run()
        try:
            if num3 == "":
                run()
            if 'n' in input("want more? y/n: ").lower():
                break
        except():
            pass

if __name__ == "__main__":
    keepRunning()
