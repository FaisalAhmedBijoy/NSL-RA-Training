'''
for strongly private  use __()
it is mainly used for classify which is subclass and superclass classification

'''
class Spam:
    __egg=7
    def print_egg(self):
        print(self.__egg)
s=Spam()
s.print_egg()
print(s._Spam__egg)