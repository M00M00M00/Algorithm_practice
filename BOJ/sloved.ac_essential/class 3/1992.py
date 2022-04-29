import sys

input = sys.stdin.readline
N = int(input())
table = [list(map(int,input().rstrip())) for _ in range(N)]

def dfs(x, y, n):
    check_num = table[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if table[i][j] != check_num:
                print('(', end = "")
                for k in range(2):
                    for l in range(2):
                        dfs(x + k * n // 2, y + l * n // 2, n //2)
                print(')', end = "")
                return ;
    if check_num == 1:
        print(1, end = "")
    else:
        print(0, end = "")
dfs(0, 0, N)
