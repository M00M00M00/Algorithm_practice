N, K = map(int,input().split())
arr = list(range(1,N + 1))
idx = 0
ans = []
while (arr):
    idx += K
    idx -= 1
    if idx > len(arr) - 1:
        idx = idx % len(arr)
    ans.append(arr[idx])
    del arr[idx]
ans = ', '.join(map(str, ans))
print(f"<{ans}>")