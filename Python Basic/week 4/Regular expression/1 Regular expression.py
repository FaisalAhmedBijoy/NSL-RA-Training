import re
pattern=r"Bangla"
result=re.match(pattern,"Bangladesh")
if result:
    print("Match found")
else:
    print("No match")