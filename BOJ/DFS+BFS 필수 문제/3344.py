def check_pos(idx, pos):
    for i in range(idx):
        if table[i] == pos:
            return False
    for i in range(idx):
        if abs(table[i] - pos) == idx - i:
            return False
    return True

def dfs(idx):
    if idx == N:
        for i in table:
            print(i + 1)
        exit()
    for i in range(N):
        if check_pos(idx, i):
            table[idx] = i
            dfs(idx + 1)
            table[idx] = -1

N = int(input())

table = [-1] * N
dfs(0)