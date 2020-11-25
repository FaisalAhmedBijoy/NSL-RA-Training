import re
pattern=r"Bangladesh" 
if re.search(pattern,"This is Bangladesh in Asia"):
    print("Match found")
else:
    print("No Match")
pattern=r"bangla"
print(re.findall(pattern,"Bangadeshi bangla ans indian bangla song"))

