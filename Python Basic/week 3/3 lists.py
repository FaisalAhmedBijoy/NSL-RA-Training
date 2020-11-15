n=int(input())
lst=[]
for i in range(n):
    operation=input().strip().split(" ")
    if operation[0] =='insert':
        lst.insert(int(operation[1]),int(operation[2]))
    elif operation[0]== 'print':
        print(lst)
    elif operation[0] == 'remove':
        lst.remove(int(operation[1]))
    elif operation[0]=='append':

        lst.append(int(operation[1]))
    elif operation[0]=='sort':
        lst.sort()
    elif operation[0]=='pop':
        lst.pop()
    elif operation[0]=='reverse':
        lst.reverse()
    
        
    