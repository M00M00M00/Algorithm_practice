N, M = map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))
    
print(arr[1:3][0:4])

