import collections
from itertools import count

N=int(input())
arr=[]
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)
counter=collections.Counter(arr)
arr_set=list(set(arr))
count_arr=[counter[arr_set[i]] for i in range(len(arr_set))]
sw = True
temp=0
cnt=0
count_num=0
ans_list=[]
while sw:
    count_num += count_arr[cnt]
    temp = arr[count_num-1] * (count_num)
    ans_list.append(temp)
    cnt+=1
    if cnt == len(count_arr):
        sw = False
print(max(ans_list))