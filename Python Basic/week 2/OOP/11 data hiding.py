'''
data are punlic or private. so data hiding is important for access modifier
_function_namae() is used to declared private og a method
private attribute or method can be accessible from it own class
'''
class Queue:
    def __init__(self,contents):
        self._hiddenlist=list(contents)
    def push(self,value):
        self._hiddenlist.insert(0,value)
    def pop(self):
        return self._hiddenlist.pop(-1)
    def _show_list(self):
        return self._hiddenlist 
queue=Queue([1,2,3])
print(queue._hiddenlist)

queue.push(10)
print(queue._hiddenlist)

queue.pop()
print(queue._hiddenlist)

print(queue._show_list())

