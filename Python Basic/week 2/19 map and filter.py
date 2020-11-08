'''
map function requires a function and iterable
'''
def make_double(x):
    return x*2
marks=[10,20,30,40]
result=map(make_double,marks)
print(result)
print(list(result))

'''
filter is used to remove some values in a perticular list
Boolean True False is used to filter the map
'''
def is_even(x):
    if x%2 ==0:
        return x
numbers=[1,2,3,4,5,6]
result=filter(is_even,numbers)
print(list(result))

'''
map filter lambda is combined used 
'''
num=[10,11,12,13,14,15]
result=list(filter(lambda x: x%2 ==0,num))
print(result)

