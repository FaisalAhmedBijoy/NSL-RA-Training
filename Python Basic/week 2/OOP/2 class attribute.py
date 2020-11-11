'''
Class has some attribute and method(function)

if a attribute can access all the object then it is called class attribute
(identity) 
'''
class Monster:
    identity="Negative character"
    def __init__(self,color,heads):
        self.color=color
        self.heads=heads
    def attack(self):
        print("Just attacked a Hero")
# Create object /instances

mournsnake=Monster("Yellow",4)
print("I am a "+str(mournsnake.heads)+'headed monster')
mournsnake.attack()
print(mournsnake.identity)


