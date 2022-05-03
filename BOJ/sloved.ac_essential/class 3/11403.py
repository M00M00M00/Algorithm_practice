from collections import deque

def bfs(n):
    global can_go

    visited = [0] * N
    q = deque([n])
    while q:
        x = q.popleft()
        for i in range(N):
            if not visited[i] and relation[x][i]:
                can_go[n][i] = 1
                visited[i] = True
                q.append(i)

N = int(input())
relation = [list(map(int,input().split())) for _ in range(N)]
can_go = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    bfs(i)

for i in can_go:
    for j in i:
        print(j, end = " ")
    print()
