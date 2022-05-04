import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())
table = [[] for _ in range(H)]
for i in range(H):
    for _ in range(N):
        table[i].append(list(map(int, input().split())))

q1 = deque([])
q2 = deque([])
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

for i in range(len(table)):
    for j in range(len(table[i])):
        for k in range(len(table[i][j])):
            if table[i][j][k] == 1:
                q1.append([i, j, k])
                visited[i][j][k] = True

cnt = -1
add_list = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]

while (q1 or q2):
    cnt += 1
    if q1:
        while q1:
            x = q1.popleft()
            for i in add_list:
                n_x, n_y, n_h = x[0] + i[0], x[1] + i[1], x[2] + i[2]
                if 0 <= n_x < H and 0 <= n_y < N and 0 <= n_h < M:
                    if not visited[n_x][n_y][n_h] and table[n_x][n_y][n_h] == 0:
                        visited[n_x][n_y][n_h] = True
                        table[n_x][n_y][n_h] = 1
                        q2.append([n_x, n_y, n_h])
    else:
        while q2:
            x = q2.popleft()
            for i in add_list:
                n_x, n_y, n_h = x[0] + i[0], x[1] + i[1], x[2] + i[2]
                if 0 <= n_x < H and 0 <= n_y < N and 0 <= n_h < M:
                    if not visited[n_x][n_y][n_h] and table[n_x][n_y][n_h] == 0:
                        visited[n_x][n_y][n_h] = True
                        table[n_x][n_y][n_h] = 1
                        q1.append([n_x, n_y, n_h])

for i in table:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()

print(cnt)
