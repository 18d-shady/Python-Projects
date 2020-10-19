# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    t = int(input())
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        lst = [] 
        try:
            ele = input()
        except EOFError:
            break 
        lst.append(ele)
        lst = '\n'.join(lst)  
        try:
            nn = int(input())
        except EOFError:
            break
        lstt = []   
        try:
            elem = input()
        except EOFError:
            break 
        lstt.append(elem)
        lstt = '\n'.join(lstt) 
        
        flag = 0
        
        if(set(lst).issubset(set(lstt))): 
            flag = 1
        if len(lstt)>300:
            flag = 0
           
        if (flag) : 
            print(True) 
        else : 
            print(False) 


for i in range(int(raw_input())): 
    a = int(raw_input()); A = set(raw_input().split()); 
    b = int(raw_input()); B = set(raw_input().split());
    print A <= B
