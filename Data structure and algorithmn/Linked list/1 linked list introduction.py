'''
A=10
B=11
C=12
A->next=B
B->next=C
'''
class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
a=ListNode(10)
b=ListNode(11)
c=ListNode(12)

a.next=b
b.next=c

print(a.data)
print(a.next.data)
print(a.next.next.data)