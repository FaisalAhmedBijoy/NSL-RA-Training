'''
product and permutation are mathematical operation
'''
from itertools import product,permutations
letters=("A","B")

print(list(product(letters,range(2))))
print(list(permutations(letters)))
