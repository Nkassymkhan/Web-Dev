import re

pattern = r'^[789][0-9]{9}$'
n = int(input())
for _ in range(n):
    if re.search(pattern, input()):
        print("YES")
    else:
        print("NO")
    