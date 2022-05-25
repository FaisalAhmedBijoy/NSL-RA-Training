
from itertools import combinations_with_replacement


#strings=str(input())
#k=int(input())
#strings='HACK'
#k=2
strings,k=input().split(' ')
#print(*permutations(strings,k))


for i in combinations_with_replacement(sorted(strings),int(k)):
    print("".join(i))