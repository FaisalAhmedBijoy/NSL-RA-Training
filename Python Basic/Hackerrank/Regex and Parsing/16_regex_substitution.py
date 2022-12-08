"""
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
Sample Output

a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.  

"""

import re
number_of_test_case=int(input())
for _ in range(number_of_test_case):
    test_case=input()
    test_case=re.sub(r'(?<= )(&&)(?= )', 'and', test_case)
    test_case=re.sub(r'(?<= )(\|\|)(?= )', 'or', test_case)
    print(test_case)
