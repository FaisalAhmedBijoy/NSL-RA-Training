'''
decimal : 233 to binary :11101001
[1, 0, 0, 1, 0, 1, 1, 1]
[1, 0, 0, 1, 0, 1, 1, 1]
<class 'str'>
11101001
'''
from data_structure import Stack
def dec2bin(decimal):
    s=Stack()
    while decimal>0:
        remainder=decimal%2
        s.push(remainder)
        decimal=decimal//2
    print(s.items)
    binary_array=s.items
    print(binary_array)
    binString=""
    while not s.isEmpty():
        top=s.pop()
        binString=binString + str(top)
    print(type(binString))
    return binString
    
print(dec2bin(233))