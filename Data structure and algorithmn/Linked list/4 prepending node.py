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


head=a
print("First node address is the head : ",head)
print("Insert New node in linked list")
item=int(input("Enter new item"))
newNode=ListNode(item)
newNode.data=item
newNode.next=head
head=newNode
print("New head: ",head)