N=int(input())
table=[[0 for _ in range(N+2)] for _ in range(N+2)]

inputTable=[]
for _ in range(N):
    inputTable.append(list(map(int,input())))

for i in range(N):
    for j in range(N):
        table[i+1][j+1] = inputTable[i][j]
def sumlist(arr):
    cnt=0
    for i in arr:
        for j in i:
            cnt+=j
    return cnt

print(sumlist(table))