'''
if we want to change any funcitonality of a function but not change the code. 
then decorator is used to modify and extend the code

'''
def my_decorator(func):
    def decorate():
        print("------------")
        func()
        print("------------")
    return decorate
    
def print_raw():
    print("Hello world")
decorated_funciton=my_decorator(print_raw)
decorated_funciton()

@my_decorator
def print_text():
    print("Faisal Ahmed Bijoy")

print_text()