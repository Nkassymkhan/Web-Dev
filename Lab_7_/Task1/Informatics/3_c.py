a = int(input())
b = int(int(input())**(1/2))+1
print(*(i**2 for i in range(a, b)))