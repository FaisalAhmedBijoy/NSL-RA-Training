'''
Infix to postfix evaluation
Reloaded modules: data_structure
Token list :  ['A', '*', 'B', '+', 'C', '*', 'D']
Precidence :  {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
Current token :  A
Stack :  []
Postfix list []



Current token :  *
Stack :  []
Postfix list ['A']



Current token :  B
Stack :  ['*']
Postfix list ['A']



Current token :  +
Stack :  ['*']
Postfix list ['A', 'B']



Stack peek :  *
Current token :  C
Stack :  ['+']
Postfix list ['A', 'B', '*']



Current token :  *
Stack :  ['+']
Postfix list ['A', 'B', '*', 'C']



Current token :  D
Stack :  ['+', '*']
Postfix list ['A', 'B', '*', 'C']



AB*CD*+
Token list :  ['(', 'A', '*', 'B', ')', '+', '(', 'C', '*', 'D', ')']
Precidence :  {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
Current token :  (
Stack :  []
Postfix list []



Current token :  A
Stack :  ['(']
Postfix list []



Current token :  *
Stack :  ['(']
Postfix list ['A']



Current token :  B
Stack :  ['(', '*']
Postfix list ['A']



Current token :  )
Stack :  ['(', '*']
Postfix list ['A', 'B']



Current token :  +
Stack :  []
Postfix list ['A', 'B', '*']



Current token :  (
Stack :  ['+']
Postfix list ['A', 'B', '*']



Current token :  C
Stack :  ['+', '(']
Postfix list ['A', 'B', '*']



Current token :  *
Stack :  ['+', '(']
Postfix list ['A', 'B', '*', 'C']



Current token :  D
Stack :  ['+', '(', '*']
Postfix list ['A', 'B', '*', 'C']



Current token :  )
Stack :  ['+', '(', '*']
Postfix list ['A', 'B', '*', 'C', 'D']



AB*CD*+
'''
from data_structure import Stack
import string
def infix2postfix(expression):
    prec={}
    prec['*']=3
    prec['/']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1
    s=Stack()
    postfixList=[]
    tokenList=expression.split()
    print('Token list : ',tokenList)
    print('Precidence : ',prec)
    for token in tokenList:
        print("Current token : ",token)
        print("Stack : ",s.items)
        print("Postfix list",postfixList)
        print("\n\n")
        
        if token in string.ascii_uppercase or token in string.digits:
            postfixList.append(token)
        elif token =='(':
            s.push(token)
        elif token ==')':
            top=s.pop()
            #print("Found ) : stack top :----------- ",top)
            while top !='(':
                
                postfixList.append(top)
                top=s.pop()
                #print("while ( :-----------> ",top)
        else:
            while (not s.isEmpty()) and (prec[s.peek()] >=prec[token]):
                print("Stack peek : ", s.peek())
                postfixList.append(s.pop())
            s.push(token)
    while not s.isEmpty():
        postfixList.append(s.pop())
    return "".join(postfixList)
            
    
print(infix2postfix("A * B + C * D"))
print(infix2postfix(" ( A * B ) + ( C * D ) "))