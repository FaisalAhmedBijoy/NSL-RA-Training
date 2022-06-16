#super class
class Image:
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height

        print(" This is super class") 

# child class
class FlowerImage(Image):
    def __init__(self, width, height) -> None:
        super().__init__(width, height)

        print("This is child class")

obj=FlowerImage(20,40)
print(obj.width,obj.height)