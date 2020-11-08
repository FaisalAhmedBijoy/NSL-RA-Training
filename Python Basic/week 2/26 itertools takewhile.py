'''
takewhile is work in a time/value condition
'''
from itertools import takewhile
numbers=[1,2,3,4,5,6,7,8,9,10]
less_than_six=takewhile(lambda x:x<=6,numbers)
filtered_numbers=list(less_than_six)
print(filtered_numbers)
