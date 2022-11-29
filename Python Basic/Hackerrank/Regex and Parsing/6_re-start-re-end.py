"""
import re
m = re.search(r'\d+','1234')
print(m.group())
print(m.start())
print(m.end())
"""
"""
Task
You are given a string .
Your task is to find the indices of the start and end of string  in .

Input Format

The first line contains the string .
The second line contains the string .

Output Format

Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

Sample Input
aaadaa
aa
Sample Output
(0, 1)  
(1, 2)
(4, 5)
"""
import re
s = str(input())
k = str(input())
m = tuple(re.finditer(r"(?=("+k+"))",s))
print(m)
if not m:
    print((-1,-1))
else:
    for i in m:
        print((i.start(),i.start()+len(k)-1))
