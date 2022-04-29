import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
table = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
num_table = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    table[a][b], table[b][a] = 1, 1
temp = 100 * 100
ans = 0

for i in range(1, N + 1):
    selected = [False] * (N + 1)
    selected[i] = True
    q1 = deque([i])
    q2 = deque()
    cnt = 0
    while (q1 or q2):
        cnt += 1
        if (q1):
            while q1:
                x = q1.popleft()
                for j in range(1, N + 1):
                    if not selected[j] and table[x][j]:
                        selected[j] = True
                        q2.append(j)
                        num_table[j][i] = cnt
                        num_table[i][j] = cnt
        else:
            while q2:
                x = q2.popleft()
                for j in range(1, N + 1):
                    if not selected[j] and table[j][x]:
                        selected[j] = True
                        q1.append(j)
                        num_table[i][j] = cnt
                        num_table[j][i] = cnt

for i in range(1, N + 1):
    kevin_num = sum(num_table[i])
    if kevin_num < temp:
        temp = kevin_num
        ans = i
print(ans)