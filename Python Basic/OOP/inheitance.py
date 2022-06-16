class A:
    def f(self):
        print(" f from class A")
class B:
    def f(self):
        print('f from class B')
class C(A,B):
    pass
obj=C()
obj.f()