class  Layer:
    def __init__(self,name) -> None:
        self.name = name
    def __call__(self,x):
        self.x=x
        print('Call function',self.x) 

layer=Layer('layer name')
print(layer.name)
print('Fucntion call as onject\n',layer('Image'))

