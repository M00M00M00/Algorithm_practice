a, b = map(int,input().split())
arr = list(map(int,input().split()))
start, end = 1, max(arr)
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            cnt += i - mid
    if cnt >= b:
        start = mid + 1
    else:
        end = mid - 1
print(end)