# stack implement using append and pop
# seq : bottom 10,20,faisal : top
# top : faisal
# pop : faisal
'''
append, pop : O(1)
insert, pop : O(n)
'''
class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items ==[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]

s=Stack()
print("Stack is created")
print("isEmpty : ",s.isEmpty())
s.push(10)
s.push(20)
s.push('faisal')
print("Current stack : ",s.items)

print('pop stack : ',s.pop())
print('peek :',s.peek())
print('size: ',len(s.items))