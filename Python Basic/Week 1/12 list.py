number=1
my_numbers=[number,2,3]
things=["numbers",0,my_numbers,4.56]
print(things)
print(things[2][2])

# list operation
first_list=[1,2,3]
print(first_list+[4,5,6])
print(first_list*3)
print(10 in first_list)
print(2 in first_list)

# slicing a list
marks=[2,4,8,16,32,64,128,256,512,1024,2048]
print(marks[2:4])
print(marks[:4])

# index jumping : jump 3 index
print(marks[2:9:3])

# list reverse
print("Reverse list")
print(marks[::-1])

#numeric operation on list
print(max(marks))
print(sum(marks))