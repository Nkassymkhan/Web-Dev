x = int(input())
if x == 1:
    d = 1
else:
    d = 1
    for i in range(1, x):
        if x % i == 0:
            d += 1
            
print(d)