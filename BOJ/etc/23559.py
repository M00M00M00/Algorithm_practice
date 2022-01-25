N,money=map(int,input().split())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))
        
arr.sort(key=lambda x : -(x[0]-x[1]))

temp=0

for i in arr:
    if i[1] >= i[0]:
        temp += 1

pos_n = ((money - (temp * 1000)) - ((N-temp) * 1000)) // 4000

cnt = 0

for i in range(len(arr)):
    if i < pos_n:
        if arr[i][1] >= arr[i][0]:
            cnt += arr[i][1]
        else:
            cnt += arr[i][0]
    else:
        cnt += arr[i][1]

print(cnt)