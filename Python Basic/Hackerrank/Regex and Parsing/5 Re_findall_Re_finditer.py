"""
Sample Input

rabcdeefgyYhFjkIoomnpOeorteeeeet
Sample Output

ee
Ioo
Oeo
eeeee
"""
import re
m=re.findall(r'([aeiouAEIOU]{2,})[^aeiouAEIOU]',input().strip())
if len(m)>0:
    for i in m:
        print(i)
else:
    print(-1)