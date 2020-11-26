# re group * means 0- infinity
import re
pattern=r'egg(spam)*'
if re.match(pattern,"egg"):
    print("Match 1")
if re.match(pattern,"eggspamsbdshbspamjsjs"):
    print("Match 2")
if re.match(pattern,"spam"):
    print("Match 3")


# group call
pattern =r'a(bc)(de)(f(g)h)i'
match=re.match(pattern,'abcdefghijkln')
if match:
    print(match)
    print(match.group())
    print(match.group(0))
    print(match.groups())