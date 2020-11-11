class Monster:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def attack(self):
        print("I'm Attacking")

class Fogthing(Monster):
    def make_sound(self):
        print("Grrrrrrrrrrr !")

class Mournsnake(Monster):
    def make_sound(self):
        print("Hissssssssssssss !")

fogthing=Fogthing("Fogthing","Yellow")
fogthing.attack()
fogthing.make_sound()

mournsnake=Mournsnake("Mournsnake","Red")
mournsnake.attack()
mournsnake.make_sound()