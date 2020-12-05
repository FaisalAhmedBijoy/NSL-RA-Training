'''
Reloaded modules: data_structure
[1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1]
BIN :  1110011000011
[3, 0, 3, 6, 1]
OCT :  16303
[3, 12, 12, 1]
HEXA :  1CC3
[1, 3]
OCT :  31
[0, 0, 1]
HEXA :  100
[0, 1]
BASE 26 :  10
'''
from data_structure import Stack
def baseConverter(decimal,base):
    digit='0123456789ABCDEF'
    s=Stack()
    while decimal>0:
        remainder=decimal%base
        s.push(remainder)
        decimal=decimal//base
    convertString=''
    print(s.items)
    while not s.isEmpty():
        top=s.pop()
        convertString=convertString+ digit[top]
        #convertString=convertString+str(top)
    return convertString
        
print("BIN : ",baseConverter(7363,2))
print("OCT : ",baseConverter(7363,8))
print("HEXA : ",baseConverter(7363,16))

print("OCT : ",baseConverter(25,8))
print("HEXA : ",baseConverter(256,16))
print("BASE 26 : ",baseConverter(26,26))