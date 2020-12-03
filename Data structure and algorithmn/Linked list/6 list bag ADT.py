class Bag:
    # constrcutur an empty bag
    def __init__(self):
        self._head=None
        self._size=0
    def __len__(self):
        return self._size
    def __contains__(self,target):
        curNode=self._head
        while curNode is not None and curNode.item !=target:
            curNode=curNode.next
        return curNode is not None
    def add(self,item):
        newNode=_BagListNode(item)
        newNode.next=self._head
        self._head=newNode
        self._size+=1
    def remove(self,item):
        predNode=None
        curNode=self._head
        while curNode is not None and curNode.item !=item:
            predNode=curNode
            curNode=curNode.next
        assert curNode is not None,"The item must be in bag"
        self._size-=1
        if curNode is _head:
            self._head=curNode.next
        else:
            predNode.next=curNode.next
            return curNode.item
    
class _BagListNode:
    def __init__(self,item):
        self.item=item
        self.next=None