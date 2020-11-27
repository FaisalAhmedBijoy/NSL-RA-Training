def search(array, key):
    begin=0
    end=len(array)-1
    index=None
    while begin<=end:
        mid=(begin+end)//2
        if key == array[mid]:
            index=mid #The value is found, save the index.
            break
        elif key > array[mid]: begin=mid+1 #Search the right portion
        elif key < array[mid]: end=mid-1 #Search the left portion
    return index #If the number is not found, index will contain None.


info=[100,2,10,50,20,500,100,150,200,1000,100]
info=sorted(info)
print(info)
while True:
    key = int(input())
    print ("Index Value: ",search(info,key))