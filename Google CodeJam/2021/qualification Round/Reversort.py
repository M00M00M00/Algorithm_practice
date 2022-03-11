N = int(input())
for j in range(N):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n):
        temp = arr[i - 1]
        inn = arr.index(i)
        arr[i - 1 : inn + 1] = sorted(arr[i - 1: inn + 1])
        cnt += inn + 1 - i + 1
    print(f"Case #{j + 1}: {cnt}")
