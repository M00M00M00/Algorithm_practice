for _ in range(int(input())):
    ans = [0, 0]
    for _ in range(int(input())):
        arr = list(map(str,input().split()))
        if int(ans[1]) < int(arr[1]):
            ans = arr
    print(ans[0])