import itertools

def dischicken(houseplace,chickenlist):
    cnt=100
    for i in chickenlist:
        temp=abs(i[0]-houseplace[0]) + abs(i[1]-houseplace[1])
        cnt=min(cnt,temp)
        if cnt==1:
            return 1
    return cnt

def wholechicken(houselist,chickenlist):
    cnt=0
    for i in houselist:
        cnt+=dischicken(i,chickenlist)
    return cnt

N,M=map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))

house=[]
chicken=[]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i,j])
        elif arr[i][j] == 2:
            chicken.append([i,j])

ans=10**6

cnt=1
for i in itertools.combinations(chicken,M):
    ans=min(ans,wholechicken(house,i))
    cnt+=1
print(ans)