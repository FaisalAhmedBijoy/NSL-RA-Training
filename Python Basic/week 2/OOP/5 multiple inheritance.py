'''
Multiple inheritance : first called Super class A
'''

class A:
    def where(self):
        print("I'm from class A")
class B:
    def where(self):
        print("I'm from class B")
class C(A,B):
    pass
an_instance_of_c= C()
an_instance_of_c.where()
print(C.mro())