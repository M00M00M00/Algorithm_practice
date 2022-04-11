import sys

def square_color(table, start, end):
    r1, c1 = start[0], start[1]
    r2, c2 = end[0], end[1]

    color = table[r1][c1]
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            if table[i][j] != color:
                return 0
    
    if color == 0:
        return 2 #white square
    elif color == 1:
        return 1 #blue square

def cnt(table, N, start, end):
    global white_num, blue_num
    if N == 1:
        if table[start[0]][start[1]] == 1:
            blue_num += 1
            return 
        white_num += 1
        return 
        
    if square_color(table, start, end) != 0:
        if square_color(table, start, end) == 2:
            white_num += 1
            return 
        blue_num += 1
        return 
    else:
        cnt(table, N//2, start, [start[0] + N//2 - 1, start[1] + N//2 - 1])
        cnt(table, N//2, [start[0], start[1] + N//2], [start[0] + N//2 - 1, end[1]])
        cnt(table, N//2, [start[0] + N//2, start[1]], [end[0], start[1] + N//2 - 1])
        cnt(table, N//2, [start[0] + N//2, start[1] + N//2], end)  
        
N = int(input())
table = []
for i in range(N):
    table.append(list(map(int,sys.stdin.readline().rstrip().split())))

white_num = 0
blue_num = 0
cnt(table, N, [0, 0], [N - 1, N - 1])

print(white_num)
print(blue_num)
