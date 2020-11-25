'''
some operation in regex
group()
start()
end()
span()
'''
import re
pattern= r'bin'
match=re.search(pattern,"combination")
if match:
    print(match)
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())