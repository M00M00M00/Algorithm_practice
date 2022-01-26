import itertools
N=int(input())
arr=[]
for _ in range(N):
    arr.append(list(map(int,input().split())))

ans=1000000

for i in itertools.combinations(range(N),N//2):
    ls1=list(i)
    ls2=list(set(range(N))-set(ls1))
    cn1=0
    cn2=0
    for j in ls1:
        for k in ls1:
            cn1 += arr[j][k]
    
    for j in ls2:
            for k in ls2:
                cn2 += arr[j][k]
    
    if abs(cn1-cn2) == 0:
        print(0)
        exit()
    else:
        ans=min(ans,abs(cn1-cn2))
print(ans)
