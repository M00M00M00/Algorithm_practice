from collections import Counter
N=int(input())
arr=list(map(int,input().split()))
M=int(input())
check=list(map(int,input().split()))
x=Counter(arr)
for i in check:
    print(x[i], end=" ")