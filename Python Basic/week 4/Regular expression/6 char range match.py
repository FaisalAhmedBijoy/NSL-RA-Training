import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "NS1 is prefix of first name server address."):
   # Found NS1 as match
   print("OK")

if re.search(pattern, "You should put a second one with NS2 as prefix."):
   # Found NS2 as match
   print("OK")

if re.search(pattern, "I don\'t have any nameserver."):
   print("NS3")
else:
   print("Not OK!")

if re.search(pattern, "PY3K"):
   # Found PY3 as match
   print("OK")
   
# ^ is used to except purpos
pattern=r"[^A-Z]"
if re.search(pattern,'all small char'):
    print("Match")