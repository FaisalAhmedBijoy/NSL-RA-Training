'''
there are some standard module which is mostly used in functional programming

count: start a define value to infinity
cycle: iterable to infinity
repeat: repeat from infinity until a value 
'''
from itertools import count
for i in count(3):
    print(i)
    if i>=11:
        break


'''
map and filter is used as a iteration manner. similarly iterable is used in 
list, dictionary.
accumulate function is used to sum up current values
'''
from itertools import accumulate
numbers=[1,2,3,4,5,6]
accumulate_number=accumulate(numbers)
print(accumulate_number)
print(list(accumulate_number))