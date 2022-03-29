from collections import deque
N = int(input())
x, y = map(int, input().split())
n = int(input())
arr = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
ans = [0 for _ in range(N + 1)]

def bfs(x):
    global ans

    q = deque([x])
    visited[x] = True
    while (q):
        c = q.popleft()
        for i in arr[c]:
            if visited[i] == 0:
                visited[i] = 1
                ans[i] = ans[c] + 1
                q.append(i)

bfs(x)

if ans[y] == 0:
    print(-1)
else:
    print(ans[y])