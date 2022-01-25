import itertools
N,S=map(int,input().split())
arr=list(map(int,input().split()))
cnt=0
for i in range(1,N+1):
    for j in itertools.combinations(arr,i):
        if sum(j) == S:
            cnt += 1

print(cnt)