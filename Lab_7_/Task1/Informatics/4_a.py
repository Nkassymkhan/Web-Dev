n = int(input())
arr = list(map(int, input().split()))

for i in range(0, n):
    ind = i
    if(ind%2 == 0):
        print(arr[ind], end = ' ')