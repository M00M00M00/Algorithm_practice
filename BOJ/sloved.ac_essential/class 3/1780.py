N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
result_minus = 0
result_zero = 0
result_plus = 0

def dfs(x, y, n):
    global result_zero, result_minus, result_plus
    check_num = table[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if table[i][j] != check_num:
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * n // 3, y + l * n // 3, n // 3)
                return ;
    if check_num == -1:
        result_minus += 1
    elif check_num == 0:
        result_zero += 1
    elif check_num == 1:
        result_plus += 1
dfs(0, 0, N)
print(result_minus)
print(result_zero)
print(result_plus)