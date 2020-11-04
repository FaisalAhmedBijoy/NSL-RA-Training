# Finally is used in 'Try except' to must run the statement
try:
    print("Hello")
    print(1/0)
except ZeroDivisionError:
    print("Divided by zero")
    print(hello)
finally:
    print("This code must run")
    