
def next(x, y, d, grid, dic):
    nx = x + dic[d][0]
    ny = y + dic[d][1]
    
    if nx < 0:
        nx = len(grid) - 1
    elif nx >= len(grid):
        nx = 0
    if ny < 0:
        ny = len(grid[0]) - 1
    elif ny >= len(grid[0]):
        ny = 0
    
    return nx, ny

def dfs(now, ori, cnt, grid):
    dic = {0:[-1, 0], 1:[0, 1], 2:[1, 0], 3:[0, -1]}
    x = now[0]
    y = now[1]
    d = now[2]
    visited[d][x][y] = 1

    nx, ny = next(x, y, d, grid, dic)
    val = grid[nx][ny]
    if val == 'R':
        d = (d + 5) % 4
    elif val == 'L':
        d = (d + 7) % 4
    if nx == ori[0] and ny == ori[1] and d == ori[2]:
        answer.append(cnt)
        return
    if not visited[d][nx][ny]:
        dfs([nx, ny, d], ori, cnt + 1, grid)


def solution(grid):
    global answer, visited
    answer = []
    visited = [[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] for _ in range(4)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                dfs([i,j,k], [i,j,k], 1, grid)
    return sorted(answer)

print(solution(["R","R"]))