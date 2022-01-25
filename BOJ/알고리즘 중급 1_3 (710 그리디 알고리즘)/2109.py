N = int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
for i in arr:
    if i[1] > 1:
        for j in range(1,i[1]):
            arr.append(i[0],j)
arr.sort(key= lambda x : (-x[1],x[0]))
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