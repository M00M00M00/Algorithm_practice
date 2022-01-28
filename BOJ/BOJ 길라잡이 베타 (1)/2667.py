import sys

N=int(sys.stdin.readline())

table=[]
for _ in range(N):
    table.append(list(map(int,sys.stdin.readline().rstrip())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def checkone(arr):
    for i in arr:
        for j in i:
            if j == 1:
                return True

    return False

def sol(arr,x,y):
    global cnt
    if (x<0 or x>N-1 or y<0 or y>N-1):
        return False
    
    if arr[x][y] == 1:
        cnt+=1
        arr[x][y] = 0
        for i in range(4):
            sol(arr,x+dx[i],y+dy[i])
        return True
    
ans=[]

cnt=0

for i in range(N):
    for j in range(N):
        if sol(table,i,j):
            ans.append(cnt)
            cnt=0

print(len(ans))
ans.sort()
for i in ans:
    print(i)