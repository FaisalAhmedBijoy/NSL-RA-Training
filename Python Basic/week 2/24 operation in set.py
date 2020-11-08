'''
Do not make use {} when call the array as set()
Remove duplicate element in a list, Set is the best tool
Set Characteristics:
    1. there is no particular sequences so indexing is not possible
    2. Every element in the set is unique
    3. it is easier to check a element which is belong or not in a set
    
'''
num={1,2,1,2,3,1,2,3}
print(num)
print(type(num))

num.add(-7)
num.remove(3)

print(num)

'''
Some mathematical operation
Union : |
Intersection : &
Difference : -
Symmetric Difference: ^
'''
first={1,2,3,4,5,6}
second={4,5,6,7,8,9}

print(first|second)
print(first&second)
print(first-second)
print(first^second)