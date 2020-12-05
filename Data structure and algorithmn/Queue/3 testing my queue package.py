'''
True
Queue :  [True, 'dog', 4]
Size :  3
Size:  2
Queue:  [8.4, True]
'''
from data_structure_package import Queue
q=Queue()
print(q.isEmpty())
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print("Queue : ",q.items)
print("Size : ",q.size())
q.enqueue(8.4)
q.dequeue()
q.dequeue()
print("Size: ",q.size())
print("Queue: ",q.items)