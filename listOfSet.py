if __name__ == '__main__':
    #declre the variables required
    setA = set()   #holds the elements in setA
    setB = set()   #holds the elements in setB
    list_of_setA = []
    list_of_setB = []

    ##get the number of tes cases
    try:
        number_of_test_case = int(input())
        ##for each test cases:
        for i in range(number_of_test_case):
            ##get the number elemente in set A
            number_of_elemnets_in_A = int(input())
            ##get the elements in set A
            setA = set()
            for j in range(number_of_elemnets_in_A):
                setA.add(int(input()))
            list_of_setA.append(setA)
            j = 0
            ##get the number elemente in set B
            number_of_elemnets_in_B = int(input())
            ##get the elements in set B
            setB = set()
            for k in range(number_of_elemnets_in_B):
                setB.add(int(input()))
            list_of_setB.append(setB)
            k = 0

        print(list_of_setA)
        print(list_of_setB)
        
        ##for each test cases:
##        for l in range(number_of_test_case):
##            ##test if set A is a subset of set B
##            ##print the true or false
##            if list_of_setA[l].issubset(list_of_setB[l]):
##                print(True)
##            else:
##                print(False)
        

    except ValueError as error:
        print(error)

