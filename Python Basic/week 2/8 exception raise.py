# it is possible to create own exception in python
print("Hello")
'''
raise NameError("Hi")
raise TypeError
'''
print("Surprisely raise show the type of error")
try:
    num=5/0
except:
    print("Custom message about an error !")
    raise