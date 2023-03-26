if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    r = sorted(arr)
    new_list = set(r)
    new_list.remove(max(new_list))
    print(max(new_list))