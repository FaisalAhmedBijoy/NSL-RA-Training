import re
n=int(input())
for i in range(n):
    print(bool(re.match(r'[-+]?[0-9]*[.][0-9]+$',input())))
    