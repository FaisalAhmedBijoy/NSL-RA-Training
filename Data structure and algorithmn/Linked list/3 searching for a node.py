'''
A=10
B=11
C=12
A->next=B
B->next=C
'''
def traversal(head):
    curNode=head
    while curNode is not None:
        print(curNode.data)
        curNode=curNode.next
        
def unorderedSearch(head,target):
    curNode=head
    while curNode is not None and curNode.data != target:
        curNode=curNode.next
    return curNode is not None

class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
a=ListNode(10)
b=ListNode(11)
c=ListNode(12)
d=ListNode(13)

a.next=b
b.next=c
c.next=d
'''
print(a.data)
print(a.next.data)
print(a.next.next.data)
'''
traversal(a)
print(unorderedSearch(a,11))
    