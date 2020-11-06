file=open("ML.txt",'r')
'''
line=file.readline()
print(line)
file.close()
'''
# file open in for loop
for line in file:
    print(line)
file.close()