"""
>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
------------------------------------------------
The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
------------
200
-----
Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned =  55+45+40+60=200 


"""
from collections import Counter

from collections import Counter
number_of_shoes = int(input())
size_of_shoes = Counter(map(int,input().split()))
customer_numbers = int(input())
total_income = []
"""
for i in range(x):
    a,b = map(int,input().split())
    if s[a] > 0:
	    total.append(b)
        s.subtract(Counter([a]))
    else:
        pass

print(sum(total))
"""
for i in range(customer_numbers):
    shoe_number, price=Counter(map(int,input().split()))
    if size_of_shoes[shoe_number]>0:
        total_income.append(price)
        size_of_shoes.subtract(Counter([shoe_number]))
    else:
        pass
print(sum(total_income))

    

