import re

total_number=int(input())
for _ in range(total_number):
    print("YES" if re.match(r'^[789]\d{9}$', input()) else "NO")

