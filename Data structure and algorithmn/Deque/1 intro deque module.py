'''
Deque: Doubly Ended Queue
Front and rear can add or pop at a time
complexities: O(1)

deque([10, 20, 30])
deque([200, 10, 20, 30, 100])
100
200
deque([10, 'Faisal', 30])
deque([10, 'Faisal', 30, 'CSE', 'KUET', 'NSL'])
deque(['Faisal', 10, 'NSL', 'KUET', 'CSE', 30])
'''
from collections import deque
d=deque([10,20,30])
print(d)
d.append(100)
d.appendleft(200)
print(d)

print(d.pop())
print(d.popleft())

d.insert(2,'Faisal')
d.remove(20)
print(d)

d.extend(['CSE','KUET','NSL'])
print(d)

d.rotate(-2)
d.reverse()
print(d)