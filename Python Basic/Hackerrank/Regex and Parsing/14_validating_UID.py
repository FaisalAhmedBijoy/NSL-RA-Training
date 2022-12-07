"""
2
B1CD102354
B1CDEF2354
Sample Output

Invalid
Valid
"""
import re
number_of_test_cases = int(input())
for _ in range(number_of_test_cases):
    uid = input()
  
    test1= re.search(r'([A-Z].*){2}', uid) 
    test2= re.search(r'([0-9].*){3}', uid) 
    test3= re.fullmatch(r'^[0-9a-zA-Z]{10}$', uid)
    
    if test1 and test2 and test3 and len(set(uid)) == 10:
        print('Valid')

    else:
        print('Invalid')