'''

inplace operator
__iadd__
__isub__
__imul__
__idiv__

'''
class Number:
    def __init__(self,value):
        self.__value=value
    def __int__(self):
        return self.__value
    def __add__(self,other):
        return self.__value + int(other) * int(other)
    def __iadd__(self,other):
        return self.__value + int(other) * int(other)
a=Number(10)
b=Number(20)
c=a+b
print(c)

a+=Number(5)
print(a)