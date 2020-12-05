from data_structure import Stack
s=Stack()
s.push(10)
s.push(20)

print(s.items)
s.push('Faisal')
s.push('ahmed')
s.push('bijoy')

s.peek()
print(s.isEmpty())
print(s.pop())
print(s.items)    