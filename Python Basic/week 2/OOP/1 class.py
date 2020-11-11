# the blueprint to create monster
class Monster:
    def __init__(self,color,heads):
        self.color=color
        self.heads=heads

# Create some real monsters
fogthing=Monster("Black",5)
mournsnake=Monster("Yellow",4)
tangleface=Monster("Red",3)

# Check wheather those monster got different existance
print(fogthing.heads)
print(fogthing.color)

print(mournsnake.heads,mournsnake.color)
print(tangleface.heads,tangleface.color)