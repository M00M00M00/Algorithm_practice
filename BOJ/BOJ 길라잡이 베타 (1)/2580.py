import sys
def isCorrect(arr,pos,x):
    sw=True
    for i in arr[pos[0]]:
        if i == x:
            return False
    
    for i in range(9):
        if arr[i][pos[1]] == x:
            return False
    
    startpoint=[pos[0]//3 * 3, pos[1]//3 * 3]
    for i in range(3):
        for j in range(3):
            if arr[startpoint[0]+i][startpoint[1]+j] == x:
                return False

    return True

table=[]
for _ in range(9):
    table.append(list(map(int,sys.stdin.readline().rstrip().split())))

zero_pos=[]

for i in range(9):
    for j in range(9):
        if table[i][j] == 0:
            zero_pos.append([i,j])

N = len(zero_pos)

def dfs(n):
    if n == N:
        for i in table:
            print(" ".join(list(map(str,i))))
        exit()


    for i in range(1,10):
        if isCorrect(table, zero_pos[n], i):
            table[zero_pos[n][0]][zero_pos[n][1]] = i
            dfs(n+1)
            table[zero_pos[n+1][0]][zero_pos[n+1][1]] = 0
            
dfs(0)