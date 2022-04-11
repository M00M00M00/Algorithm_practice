from collections import deque
import sys

def bfs(idx):
    global ans

    ans += 1
    q = deque([idx])
    while q:
        x = q.popleft()
        for i in range(1, N + 1):
            if table[x][i] and not visited[i]:
                visited[i] = True
                q.append(i)

input = sys.stdin.readline



N, M = map(int, input().split())
table = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    table[a][b] = 1
    table[b][a] = 1
visited = [False for _ in range(N + 1)]
ans = 0

for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
print(ans)