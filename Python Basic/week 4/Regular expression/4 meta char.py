'''
meth character is used to solve complex pattern or logic
.dot() : 
'''
import re
pattern=r"gr.y"
if re.match(pattern,"grey"):
    print("Match 1")
if re.match(pattern,"gray"):
    print("Match 2")
if re.match(pattern,"blue"):
    print("Match 3")
    
'''
another meta char is : ^ and $ which is used to check 
start and end of a string

'''
pattern=r'^wr.te$'
#pattern=r'^wrxxxxxxte$'
if re.match(pattern,"write"):
    print("Match 1")
if re.match(pattern,"wrote"):
    print("Match 2")
if re.match(pattern,"writer"):
    print("Match 3")