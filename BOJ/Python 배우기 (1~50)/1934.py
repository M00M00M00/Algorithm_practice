for _ in range(int(input())):
    a,b = map(int,input().split())
    temp = a
    while True:
        if temp % b == 0:
            print(temp)
            break
        else:
            temp += a