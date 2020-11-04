# assert is used to check quickly any statement true or false
# it is called as sanity check
print(1)
assert 2+2 ==4
print(2)
#assert 1+1 ==3
print(3)


# progeammer are used assert to check a data or function

def KelvinToFahren(temperature):
    assert temperature>=0, "colder than absolute error"
    return (temperature-273)*1.8 + 32
print(KelvinToFahren(273))
print(int(KelvinToFahren(505.5)))
print(KelvinToFahren(-10))
    
