from collections import deque

N, M = map(int, input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input())))
dist = [[0 for _ in range(M)] for _ in range(N)]
dist[0][0] = 1

def bfs():
    q = deque()
    q.append((0 ,0))
    while (q):
        x = q.popleft()
        if (x[0] == N - 1 and x[1] == M - 1):
            print(dist[N - 1][M - 1])
            exit()
        for i in ((x[0] + 1, x[1]), (x[0] - 1, x[1]), (x[0], x[1] + 1), (x[0], x[1] - 1)):
            if (0 <= i[0] < N) and (0 <= i[1] < M) and not dist[i[0]][i[1]] and arr[i[0]][i[1]]:
                dist[i[0]][i[1]] = dist[x[0]][x[1]] + 1
                q.append(i)

bfs()