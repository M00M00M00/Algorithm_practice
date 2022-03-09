n = int(input())
arr = list(map(int,input().split()))
start, end = 0, max(arr)
target = int(input())
while start <= end:
    mid = (start + end) // 2
    log = 0
    for i in arr:
        if i >= mid:
            log += mid
        else:
            log += i
    if log > target:
        end = mid - 1
    else:
        start = mid + 1
print(end)