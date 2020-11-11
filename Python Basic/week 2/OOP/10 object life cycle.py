'''
Object has three duration of its life cycle 
1. Creation
2. Manipulation
3. Destrcution

init is called to allocate memory. Grabage collector is free the memory 
after destroy the object
'''
class Add:
    ## initialization 
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b

obj=Add(3,4)
## Access

print(obj.add())
## Destroy

'''
Reference count
if a variable is not used then Memory management automatically delete it
it can be delete manually using del keyword
'''
# reference count increase
a=42
b=a
c=[a]
# reference decrease
del a
b=100
c[0]=-1

