
"""

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

------Output--------
AB
CA
AD

"""
from email.policy import default

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        uniq = ''
        for c in string[i : i+k]:
            if (c not in uniq):
                uniq+=c
        print(uniq)

if __name__ == '__main__':
    string, k = input(), int(input())
    #string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)
