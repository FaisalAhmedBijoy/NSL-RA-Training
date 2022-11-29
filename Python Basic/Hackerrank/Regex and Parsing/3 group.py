import re
m=re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
print(m.group())
print(m.group(1))
print(m.group(1,2,3))
print(m.groups())

print(" gropus dict")
m=re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>)\w+','username@hackerrank.com')
print(m.groupdict())