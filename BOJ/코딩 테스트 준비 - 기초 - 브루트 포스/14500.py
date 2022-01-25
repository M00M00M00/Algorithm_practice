N, M = map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))
ans=0

######ㅡshape######
for i in range(N):
    for j in range(M-3):
        ans = max(ans, sum(arr[i][j:j+4]))

for j in range(M):
    for i in range(N-3):
        cnt=0
        for k in range(4):
            cnt+=arr[i+k][j]
        ans = max(ans, cnt)
    
#######ㅁshape#######
for i in range(N-1):
    for j in range(M-1):
        ans = max(ans, arr[i][j] + arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1])

#######ㄴshape#######
for i in range(N-1):
    for j in range(M-2):
        arr_sum=sum(arr[i][j:j+3]) + sum(arr[i+1][j:j+3])
        x=min(arr[i][j]+arr[i][j+1],arr[i][j+1]+arr[i][j+2],
            arr[i+1][j]+arr[i+1][j+1],arr[i+1][j+1]+arr[i+1][j+2])
        ans=max(ans, arr_sum-x)
        
for i in range(N-2):
    for j in range(M-1):
        arr_sum=sum(arr[i][j:j+2]) + sum(arr[i+1][j:j+2]) + sum(arr[i+2][j:j+2])
        x=min(arr[i][j]+arr[i+1][j],arr[i+1][j]+arr[i+2][j],
            arr[i][j+1]+arr[i+1][j+1],arr[i+1][j+1]+arr[i+2][j+1])
        ans=max(ans, arr_sum-x)

########ㄹshape########
for i in range(N-1):
    for j in range(M-2):
        arr_sum=sum(arr[i][j:j+3]) + sum(arr[i+1][j:j+3])
        x=min(arr[i][j]+arr[i+1][j+2],arr[i][j+2]+arr[i+1][j])
        ans=max(ans, arr_sum-x)
        
for i in range(N-2):
    for j in range(M-1):
        arr_sum=sum(arr[i][j:j+2]) + sum(arr[i+1][j:j+2]) + sum(arr[i+2][j:j+2])
        x=min(arr[i][j]+arr[i+2][j+1],arr[i][j+1]+arr[i+2][j])
        ans=max(ans, arr_sum-x)

########ㅗshape########
for i in range(N-1):
    for j in range(M-2):
        arr_sum=sum(arr[i][j:j+3]) + sum(arr[i+1][j:j+3])
        x=min(arr[i][j]+arr[i][j+2],arr[i+1][j]+arr[i+1][j+2])
        ans=max(ans, arr_sum-x)
        
for i in range(N-2):
    for j in range(M-1):
        arr_sum=sum(arr[i][j:j+2]) + sum(arr[i+1][j:j+2]) + sum(arr[i+2][j:j+2])
        x=min(arr[i][j]+arr[i+2][j],arr[i][j+1]+arr[i+2][j+1])
        ans=max(ans, arr_sum-x)
        
print(ans)