'''
Working with file, always use Try exepct finally.
finally is used to close the file must,if the program may got any error
'''
try:
    file=open('test.txt','r')
    content=file.read()
    print(content)
finally:
    file.close()
    
'''
another standard way is to 'with' statement. with is a temporay variable
so that execution the statement the file destroy automatically

'''
with open('ML.txt') as f:
    print(f.read())