import itertools
N,M=map(int,input().split())
arr=list(map(int,input().split()))    
a=itertools.combinations(sorted(arr),M)
for i in a:
    for j in i:
        print(j,end=" ")
    print()