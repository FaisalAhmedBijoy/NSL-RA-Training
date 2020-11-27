'''
in loop ,it is recommed to not use strlen() 
because strlen() complexity is O(n)
everytime the strlen call then complexity O(n2)
'''
def algo(s):
    c=0
    for i in range(len(s)):
        if s[i]=='a':
            c=c+1
    return c
print(algo("faisal"))