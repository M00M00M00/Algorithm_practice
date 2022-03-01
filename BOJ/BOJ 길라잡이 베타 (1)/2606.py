
def dfs(n):
    global cnt
    
    visited[n] = 1
    for i in range(len(link[n])):
        if link[n][i]:
            if visited[i] == 0:
                cnt+= 1
                dfs(i)

x = int(input())
n = int(input())
visited = [0 for _ in range(x + 1)]
link = [[0 for _ in range(x + 1)] for _ in range(x + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    link[a][b] = 1
    link[b][a] = 1
cnt = 0
dfs(1)
print(cnt)