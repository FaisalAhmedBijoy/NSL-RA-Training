# file write(filename,mode: w)
file=open('test.txt','w')
file.write("Faisal ahmed bijoy")
file.close()

file=open('test.txt','r')
content=file.read()
print(content)
file.close()