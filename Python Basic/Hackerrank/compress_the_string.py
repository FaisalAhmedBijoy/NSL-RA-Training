"""
Input: 1222311
Output: (1, 1) (3, 2) (1, 3) (2, 1)

"""
from itertools import groupby
#input_string='1222311'
input_string=input()
for i,items in groupby(input_string):
    #print(i)
    #print(len(list(items)))
    number=len(list(items))
    print(f'({number}, {i})',end=' ')