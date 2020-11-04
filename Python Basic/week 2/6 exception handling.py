# divisiob bt 0 handling
try:
    a=10
    b=int(input('Enter a value : '))
    print(a/b)
except ZeroDivisionError:
    print("Divided by 0 is not possible")

# value error and type error handle
try:
    var=10
    print(var+10)
    print(var+'hello')
    print(var/2)
except ZeroDivisionError:
    print("Divided by zero")
except(ValueError,TypeError):
    print("Type or Value error")
except:
    print("Unknown error occur")