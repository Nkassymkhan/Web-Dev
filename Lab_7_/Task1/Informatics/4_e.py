n = int(input())
arr = list(map(int, input().split()))

ok = False
for i in range(1, n):
    if (arr[i-1] * arr[i] > 0):
        ok = True

if(ok):
    print("YES")
else:
    print("NO")