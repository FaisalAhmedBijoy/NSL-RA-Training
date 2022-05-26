"""
>>> phase(complex(-1.0, 0.0))
3.1415926535897931

>>> abs(complex(-1.0, 0.0))
1.0

------------------
Input
1+2j
Output
2.23606797749979 
1.1071487177940904
"""


import cmath
print(*cmath.polar(complex(input())), sep='\n')