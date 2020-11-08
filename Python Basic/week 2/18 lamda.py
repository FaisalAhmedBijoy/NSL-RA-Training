'''

lambda x,y : x+y
lambda  parameter: operation with the parameter
'''
def my_function(func,arg):
    return func(arg)
print(my_function(lambda x:2*x,5))

print((lambda x,y:x+2*y)(2,3))