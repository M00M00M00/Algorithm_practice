import sys

N,M,B = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
ans = 500 * 500 * 256 * 2
anss = 0
e = 257
for i in range(e):
    mmax = 0
    mmin = 0
    for j in range(len(arr)):
        for k in range(len(arr[0])):
            if arr[j][k] < i:
                mmin += i - arr[j][k]
            else:
                mmax += (arr[j][k] - i)
    inven = mmax + B - mmin
    if inven < 0:
        continue
    time = 2 * mmax + mmin
    if time <= ans:
        ans = time
        anss = i
    
print(ans, anss)