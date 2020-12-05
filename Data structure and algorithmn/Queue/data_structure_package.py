"""
enqueue:
    position: insert 0 , rear ,first item of list
    complexity :O(1)
dequeue :
    pop : front , last item of the list
    complexity: O(n)

"""
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
