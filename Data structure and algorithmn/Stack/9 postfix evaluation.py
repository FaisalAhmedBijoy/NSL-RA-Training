'''
postfix evaluation:
    Reloaded modules: data_structure
['4', '5', '6', '*', '+']
Stack :  []
Stack :  ['4']
Stack :  ['4', '5']
Stack :  ['4', '5', '6']
Stack :  ['4', 30]
34
['7', '8', '+', '3', '2', '+', '/']
Stack :  []
Stack :  ['7']
Stack :  ['7', '8']
Stack :  [15]
Stack :  [15, '3']
Stack :  [15, '3', '2']
Stack :  [15, 5]
3.0

exercise: 
    10 + 3 * 5 / (16 - 4) -> 10 3 5 * 16 4 - / +
    17 10 + 3 * 9 / == 9
    
    
'''
from data_structure import Stack
import string
def domath(first,op,second):
    if op =='+':
        return first+second
    elif op =='-':
        return first-second
    elif op =='*':
        return first * second
    elif op=='/':
        return first/second
def postfixEvaluation(expression):
    s=Stack()
    tokenList=expression.split()
    print(tokenList)
    operators=['+','-','*','/']
    for token in tokenList:
        print("Stack : ",s.items)
        
        if token in string.digits:
            s.push(token)
        elif token in operators:
            second=s.pop()
            first=s.pop()
            result=domath(int(first),token,int(second))
            s.push(result)
    return s.pop()
print(postfixEvaluation(' 4 5 6 * + '))
print(postfixEvaluation(' 7 8 + 3 2 + / '))
