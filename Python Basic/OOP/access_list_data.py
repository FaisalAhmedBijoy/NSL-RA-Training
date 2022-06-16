class LaptopBrand:
    def __init__(self,name=None):
        self.name = name
        return list(self.name)

laptopBrand=LaptopBrand()
print(laptopBrand.name)

laptopBrand[0]='DELL'
laptopBrand[1]='HP'

print(laptopBrand[0])