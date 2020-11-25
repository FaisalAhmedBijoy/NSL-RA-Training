import re
n=int(input())
for i in range(n):
    try:
        ans=True
        value=input()
        regex=re.compile(value)
    except re.error:
        ans=False
    print(ans)