def delete_node(head,item):
    predNode=head
    curNode=head
    while curNode is not None and curNode.data != item:
        predNode=curNode
        curNode=curNode.next
    if curNode is not None:
        if curNode is head:
            head=curNode.next
        else:
            predNode.next=curNode.next
    

def traverse_node(head):
    curNode=head
    while curNode is not None:
        print(curNode.data)
        curNode=curNode.next
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
print("First: ",a.data)
print("Second: ",a.next.data)
print("Third: ",a.next.next.data)
print("Fourth: ",d.data)


head=a
print("First node address is the head : ",head)
print("Insert delete node in linked list")
item=int(input("Enter item : "))
delete_node(head,item)
traverse_node(head)
