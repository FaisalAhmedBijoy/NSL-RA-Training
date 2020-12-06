'''
Hot potato
Reloaded modules: data_structure_package
Name List :  ['Brad', 'Kent', 'Jane', 'Susan', 'David', 'Bill']
Deque name:  David
Queue :  ['Bill', 'Brad', 'Kent', 'Jane', 'Susan'] 

Deque name:  Kent
Queue :  ['Jane', 'Susan', 'Bill', 'Brad'] 

Deque name:  Jane
Queue :  ['Susan', 'Bill', 'Brad'] 

Deque name:  Bill
Queue :  ['Brad', 'Susan'] 

Deque name:  Brad
Queue :  ['Susan'] 

Susan
'''
from data_structure_package import Queue
def hotpotato(namelist,num):
    q=Queue()
    for name in namelist:
        q.enqueue(name)
    print("Name List : ",q.items)
    while q.size()>1:
        for i in range(num):
            q.enqueue(q.dequeue())
        
        
        print("Deque name: ",q.dequeue())
        print("Queue : ",q.items,'\n')
    return q.dequeue()
    
namelist=['Bill','David','Susan','Jane','Kent','Brad']
print(hotpotato(namelist,7))