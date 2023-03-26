n = int(input())
a = list(map(int, input().split()))

while (n > 0):
    print(a[n - 1], end = " ")
    n -= 1