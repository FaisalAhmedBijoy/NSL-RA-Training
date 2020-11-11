'''
Priority is base class first then the super class
called subclass attribute and method first
'''

class Monster:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def attack(self):
        print('I am attacking...')


class Fogthing(Monster):
    def attack(self):
        print('I am killing...')

    def make_sound(self):
        print('Grrrrrrrrrr\n')


fogthing = Fogthing("Fogthing", "Yellow")
fogthing.attack()
fogthing.make_sound()