'''
Complexity of a binary search is O(log2n)
instead of O(n)

it is used to check a particular value in a array list
'''
def BinarySearch(n,val,key):
    low=1
    high=n
    while(low<=high):
        mid=(low+high)//2
        if key<val[mid]:
            low=mid+1
        elif key>val[mid]:
            high=mid+1
        elif key==val[mid]:
            return 1
val=[1,2,3,4,5,6,7,8]
key=5
n=len(val)
print(BinarySearch(n,val,key))