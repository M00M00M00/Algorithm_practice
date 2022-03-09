a, b = map(int,input().split())
arr = []
for _ in range(a):
    arr.append(int(input()))
start, end = 1, max(arr)
while start <= end:
    mid = (start + end) // 2
    log = 0
    for i in arr:
        log += i // mid
    if log >= b:
        start = mid + 1
    else:
        end = mid - 1
print(end)