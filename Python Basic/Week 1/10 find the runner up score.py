n=int(input())
a=[int(i) for i in input().split()]

maxvalue=max(a)
while max(a) == maxvalue:
    a.remove(max(a))
print(max(a))
