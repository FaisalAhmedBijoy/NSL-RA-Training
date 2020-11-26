import re
# <group> group values
pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

# another meta char
import re

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
    print ("Gray is fine!")

match = re.match(pattern, "grey")
if match:
    print ("Grey is OK also!")    

match = re.match(pattern, "griy")
if match:
    print ("No way, what Griy is?!!")
    