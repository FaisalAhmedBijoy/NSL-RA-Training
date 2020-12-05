from data_structure import Stack
def parChecker(parentheses):
    s=Stack()
    index=0
    balanced=True
    while index<len(parentheses) and balanced:
        symbol=parentheses[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                s.pop()
        index=index+1
    
    if balanced and s.isEmpty():
        return True
    else:
        return False
    
    
    
    
print(parChecker('((()))'))
print(parChecker('((()'))
print(parChecker('))))))'))