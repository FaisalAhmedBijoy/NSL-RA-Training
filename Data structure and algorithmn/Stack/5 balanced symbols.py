'''
symbol:  [
symbol:  {
symbol:  (
symbol:  )
top :  (
0
0
symbol:  }
top :  {
1
1
symbol:  ]
top :  [
2
2
C1 : True
symbol:  {
symbol:  }
top :  {
1
1
symbol:  [
symbol:  ]
top :  [
2
2
symbol:  [
symbol:  ]
top :  [
2
2
symbol:  [
symbol:  ]
top :  [
2
2
symbol:  [
symbol:  ]
top :  [
2
2
symbol:  [
C2:  False
'''

from data_structure import Stack
def matches(open,close):
    opens='({['
    closes=')}]'
    print(opens.index(open))
    print(closes.index(close))
    return opens.index(open) == closes.index(close)
def parchecker(parentheses):
    index=0
    balanced=True
    s=Stack()
    while index<len(parentheses) and balanced:
        symbol=parentheses[index]
        print('symbol: ',symbol)
        if symbol in '({[':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                top=s.pop()
                print("top : ",top)
                if not matches(top,symbol):
                    balanced=False
        index=index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False
        
    
print('C1 :',parchecker('[{()}]'))

print('C2: ',parchecker('{}[][][][]['))
'''
print(parchecker('{({([][])}())}'))
print(parchecker('[{()]'))
'''