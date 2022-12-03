"""
11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   
Sample Output

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

"""

import re
n = int(input())
pattern=r'#[0-9a-fA-F]{3,6}'
for _ in range(n):
    for line in input().split('\n'):
        result=tuple(re.finditer(pattern,line))
        # print(line)
        # print(result)
        if result:
            for i in result:
                # print(i.start(),i.end())
                if i.start()!=0:
                    print(i.group())    