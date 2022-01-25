import itertools
N,M=map(int,input().split())
arr=list(map(int,input().split()))    
a=itertools.product(sorted(arr),repeat=M)
for i in a:
    for j in i:
        print(j,end=" ")
    print()