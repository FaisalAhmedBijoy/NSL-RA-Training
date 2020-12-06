'''
Palindrome cheker:
    RADAR -> Palindrome
    DHAKA _> NOT Palindrome

Reloaded modules: data_structure_package_deque
RADAR
['R', 'A', 'D', 'A', 'R']
R R
A A
True
BANGLA
['B', 'A', 'N', 'G', 'L', 'A']
A B
False
OTTO
['O', 'T', 'T', 'O']
O O
T T
True
'''
from data_structure_package_deque import Deque
def palindromeChecker(palindrome):
    print(palindrome)
    d=Deque()
    checker=True
    for c in palindrome:
        d.addFront(c)
   
    print(d.items)
    while  d.size()>1 and checker:
        first=d.removeFront()
        last=d.removeRear()
        print(first,last)
        if first != last:
            checker =False
            break
    
    return checker
        
        
    
print(palindromeChecker('RADAR'))
print(palindromeChecker('BANGLA'))
print(palindromeChecker('OTTO'))