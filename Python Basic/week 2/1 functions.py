# * argument packed as a tuple
# we pass pass arg a lot
def make_sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(make_sum(10,20,30,40))

# ** is used to pass dict parameter
def print_dict(**kwargs):
    print(kwargs)
print_dict(a=1,b=2,c=3)

#mixed paramter passing function
def print_all(a,*args,**kwargs):
    print(a)
    print(args)
    print(kwargs)
print_all(10,20,30,40,b=10,c=50)