from collections import deque

N, K = map(int, input().split())
MAX = 100000
MIN = 0
dist = [0] * (MAX + 1)

def bfs(n):
    q = deque()
    q.append(n)
    while (q):
        x = q.popleft()
        if (x == K):
            print(dist[x])
            exit()
        for i in (x + 1, x - 1, 2 * x):
            if MIN <= i <= MAX and not dist[i]:
                dist[i] = dist[x] + 1
                q.append(i)

bfs(N)