n = int(input())
if n == 1:
    print(1)
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        print(i)