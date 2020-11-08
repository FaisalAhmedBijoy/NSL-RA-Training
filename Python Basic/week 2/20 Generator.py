def my_iterable():
    i=5
    while i>0:
        yield i
        i-=1

for i in my_iterable():
    print(i)
    
'''
Even number from a list
'''
def even_numbers(n):
    for i in range(n):
        if i%2 ==0:
            yield i
even_nums=list(even_numbers(10))
print(even_nums)