from collections import deque

N, K = map(int,input().split())
arr=deque(list(range(1,N+1)))
l=N
s=K
result = []
while l:
    result.append(arr[s-1])
    arr.remove(arr[s-1])
    l -= 1
    if s == 0:
        s += K
    else:
        s += K - 1
    if s > l-1 and l != 0:
        s = s%l
print('<', end="")
for i in range(len(result)):
    if i != len(result)-1:
        print(f"{result[i]},", end=" ")
    else:
        print(result[i],end="")
print('>')
