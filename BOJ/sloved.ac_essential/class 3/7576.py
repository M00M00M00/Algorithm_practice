import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(lst):
    global ans
    q1 = deque(lst)
    q2 = deque([])
    while q1 or q2:
        ans += 1
        sw = 0
        while q1:
            sw = 1
            x = q1.popleft()
            for i in range(4):
                r1 = x[0] + dx[i]
                c1 = x[1] + dy[i]
                if 0 <= r1 < r and 0 <= c1 < c and table[r1][c1] == 0:
                    table[r1][c1] = 1
                    q2.append([r1, c1])
        if sw == 0:
            while q2:
                x = q2.popleft()
                for i in range(4):
                    r1 = x[0] + dx[i]
                    c1 = x[1] + dy[i]
                    if 0 <= r1 < r and 0 <= c1 < c and table[r1][c1] == 0:
                        table[r1][c1] = 1
                        q1.append([r1, c1])


input = sys.stdin.readline

c, r = map(int,input().split())
table = []
for _ in range(r):
    table.append(list(map(int,input().split())))
ans = -1
tomato_pos = []
for i in range(r):
    for j in range(c):
        if table[i][j] == 1:
            tomato_pos.append([i, j])

bfs(tomato_pos)
for i in range(r):
    for j in range(c):
        if table[i][j] == 0:
            print(-1)
            exit()
print(ans)