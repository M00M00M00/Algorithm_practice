import sys
from collections import deque

def bfs(arr, x, y):
    global ans

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque([[x, y]])
    arr[y][x] = 0
    ans += 1
    while (q):
        c = q.popleft()
        for i in range(4):
            x = c[0] + dx[i]
            y = c[1] + dy[i]
            if 0 <= x < M and 0 <= y < N and arr[y][x] == 1:
                q.append([x, y])
                arr[y][x] = 0


def solution(M, N, K):
    global ans
    
    ans = 0
    arr = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1
    for i in range(M):
        for j in range(N):
            if arr[j][i] == 1:
                bfs(arr, i, j)

T = int(input())
for _ in range(T):
    M, N, K = map(int,input().split())
    solution(M, N, K)
    print(ans)