import sys

sys.setrecursionlimit(10**6)

def dfs(x, y, c):
    global ans
    if (x == row - 1 and y == col - 1):
        ans = min(ans, c)
        return
    for i in range(4):
        x1 = x + dict[i][0]
        y1 = y + dict[i][1]
        if x1 < 0 or x1 > row - 1 or y1 < 0 or y1 > col - 1:
            continue
        if (table[x1][y1] == 0 and selected[x1][y1] == 0):
            selected[x1][y1] = 1
            dfs(x1, y1, c + 1)
            selected[x1][y1] = 0
        elif (table[x1][y1] == 1 and selected[x1][y1] == 0 and can_broke [0] == 1):
            selected[x1][y1] = 1
            can_broke[0] = 0
            dfs(x1, y1, c + 1)
            selected[x1][y1] = 0
            can_broke[0] = 1
            
            
 
row, col = map(int,sys.stdin.readline().rstrip().split())
table = []
can_broke = [1]
for _ in range(row):
    table.append(list(map(int, sys.stdin.readline().rstrip())))
selected = [[0 for _ in range(col)] for _ in range(row)]
selected[0][0] = 1
ans = 1000 * 1000 + 1
dict = {0:[1,0], 1:[0,1], 2:[-1,0], 3:[0,-1]}
dfs(0, 0, 1)
if ans == 1000 * 1000 + 1:
    print("-1")
else:
    print(ans)