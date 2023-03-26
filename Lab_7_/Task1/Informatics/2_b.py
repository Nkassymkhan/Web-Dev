year = int(input())
def is_leap(year):
    leap = "NO"
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = "YES"
    
    return leap

print(is_leap(year))