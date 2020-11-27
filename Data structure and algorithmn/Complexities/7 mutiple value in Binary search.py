def search(array, key):
    begin=0
    end=len(array)-1
    index=None
    while begin<=end:
        mid=(begin+end)//2
        if key == array[mid]:
            index=mid #One occurance of the value is found, save the index
            end=mid-1 #Continue searching the left portion after one occurrence is found
        elif key > array[mid]: begin=mid+1
        elif key < array[mid]: end=mid-1
    return index #Index will contain None if the value is not found
numbers=[5265,2,1,5,4,5,4,4,4,546,10]
array=sorted(numbers)
print(array)
key=int(input("Enter The key : "))
print("Index : ",search(array,key))