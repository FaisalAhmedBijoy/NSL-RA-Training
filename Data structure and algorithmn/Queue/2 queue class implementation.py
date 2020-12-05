"""
enqueue:
    position: insert 0 , rear ,first item of list
    complexity :O(1)
dequeue :
    pop : front , last item of the list
    complexity: O(n)

"""
'''
True
None
10
1
[20]
'''
class Queue:
    def __init__(self):
        self.items=[]
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

q=Queue()
print(q.isEmpty())
print(q.enqueue(10))
q.enqueue(20)
print(q.dequeue())
print(q.size())
print(q.items)


