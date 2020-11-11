'''
super keyword is used to called super class attribute or method

'''
class A:
    def spam(self):
        print("A")
class B(A):
    def spam(self):
        print("B")
        super().spam()
        
B().spam()