'''
Queue : First In First Out (FIFO)
a queue has two part: front, rear
Queue : rear [1,2,3,4,5] front
insert data in queue : put
out data from queue
1
2
Queue size :  1
Is full: False

'''
from queue import Queue
#q=Queue()
q=Queue(maxsize=10)
print("insert data in queue : put")
q.put(1)
q.put(2)
q.put(3)
print("out data from queue")
print(q.get())
print(q.get())

print("Queue size : ",q.qsize())
print("Is full:",q.full())

