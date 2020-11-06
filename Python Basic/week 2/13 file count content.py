file=open('test.txt','w')
content=file.write("CSE KUET")
if content:
    print("Yes, {0} byte has been done".format(content))
    print(content)

file.close()