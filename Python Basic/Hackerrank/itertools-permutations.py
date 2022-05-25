"""
>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
"""

"""
Input:
HACK 2

Output:
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
"""
from itertools import permutations
#strings=str(input())
#k=int(input())
#strings='HACK'
#k=2
strings,k=input().split()
#print(*permutations(strings,k))
permutated_list=list(permutations(strings,int(k)))
for i in permutated_list:
    print(''.join(i))