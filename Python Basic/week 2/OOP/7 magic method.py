class Calculator:
    def __add__(self,x,y):
        print(x+y)
c=Calculator()
c.__add__(10,20)