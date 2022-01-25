N = int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))

arr.sort(key= lambda x : (-x[1],-x[0]))

while True:
    switch_cnt=0
    for i in range(len(arr)-1):
        if arr[i][1]>1:
            if arr[i][1] == arr[i+1][1]:
                arr[i+1][1] = arr[i+1][1]-1
                switch_cnt+=1
                arr.sort(key= lambda x : (-x[1],-x[0]))
    if switch_cnt == 0:
        break

cnt=0
n_list=[]
for i in arr:
    n_list.append(i[1])
n_list=list(set(n_list))
for i in n_list:
    max_p=0
    for j in arr:
        if j[1] == i:
            max_p=max(j[0],max_p)
    cnt+=max_p
print(cnt)
