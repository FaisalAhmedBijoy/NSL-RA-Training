'''
Python list is used to build deque class
Assume rear of the deque is at position 0 in the list
'''
class Deque:
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items == []
    
    def addFront(self,item):
        return self.items.append(item)
    def addRear(self,item):
        return self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

d=Deque()
print(d.isEmpty())
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)

print(d.size())
print(d.items)
d.addRear(8.4)
print(d.removeFront())
print(d.removeRear())
print(d.items)
        