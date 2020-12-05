# stack implementation using list
# use pop,insert instead of pop,append
'''
stack seq : top: 1->2->3->4->5->6
top :1
pop item :1
insert : 0, item
num=[1,2,3,4,5,6]
print(num.pop())
print(num.insert(0,10))
print(num)
'''
class Stack:
    def __init__(self):
        self.items=[]
        print("Stack created")
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        print('push : ',self.items)
        return self.items.insert(0,item)
    def pop(self):
        print('pop : ',self.items)
        return self.items.pop(0)
    def peek(self):
        print('peek : ',self.items)
        return self.items[0]
    def size(self):
        print(len(self.items))
        # return len(sefl.items)

s=Stack()
s.push('Faisal')
s.push('ahmed')
s.push('bijoy')

s.peek()
s.size()
print(s.isEmpty())
print(s.pop())
    