from math import inf
import copy

def solution(rows, columns, queries):
    answer = []
    table = [[]for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            table[i].append(cnt)
            cnt += 1

    for i in queries:
        r1 = i[0] - 1
        c1 = i[1] - 1
        r2 = i[2] - 1
        c2 = i[3] - 1
        temp_table = copy.deepcopy(table)
        temp_min = inf
        for i in range(c1, c2): #up
            table[r1][i + 1] = temp_table[r1][i]
            temp_min = min(temp_min, temp_table[r1][i])
        for i in range(r1, r2): #right
            table[i + 1][c2] = temp_table[i][c2]
            temp_min = min(temp_min, temp_table[i][c2])
        for i in range(c2, c1, -1): #down
            table[r2][i - 1] = temp_table[r2][i]
            temp_min = min(temp_min, temp_table[r2][i])
        for i in range(r2, r1, -1): #left
            table[i - 1][c1] = temp_table[i][c1]
            temp_min = min(temp_min, temp_table[i][c2])
        answer.append(temp_min)

    return answer

solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])