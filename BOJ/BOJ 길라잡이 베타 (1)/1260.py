from collections import deque

def dfs(n):
    print(n+1,end=" ")
    visited[n] = True
    for i in range(len(arr)):
        if arr[i][n]:
            if not visited[i]:
                dfs(i)

def bfs(n):
    visited[n] = True
    que = deque([n])
    while que:
        next=que.popleft()
        print(next + 1, end=" ")
        for i in range(len(arr[next])):
            if arr[next][i]:
                if not visited[i]:
                    que.append(i)
                    visited[i] = True
        
N,M,V=map(int,input().split())
arr=[[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1


visit=[]

visited=[False] * N

dfs(V-1)
print()
visited=[False] * N
bfs(V-1)