import sys

input = sys.stdin.readline
N, M = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(1, len(arr)):
    arr[i] = arr[i] + arr[i - 1]
for _ in range(M):
    start, end = map(int, input().split())
    if start == 1:
        start = 0
    else:
        start = arr[start - 2]
    end = arr[end - 1]
    print(end - start)
