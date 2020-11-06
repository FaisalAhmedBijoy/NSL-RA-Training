def make_twice(func,arg):
    return func(func(arg))
def add_five(x):
    return x+5
print(make_twice(add_five,10))