for _ in range(int(input())):
    arr=list(map(str,input().split()))
    temp=float(arr[0])
    for i in range(1,len(arr)):
        if arr[i] == '@':
            temp *= 3
        elif arr[i] == '%':
            temp += 5
        elif arr[i] == '#':
            temp -= 7
    print(f"{temp:0.2f}")