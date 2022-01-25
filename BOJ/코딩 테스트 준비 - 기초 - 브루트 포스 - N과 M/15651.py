import itertools
N,M=map(int,input().split())
a=itertools.product(range(1,N+1),repeat=M)
for i in a:
    for j in i:
        print(j,end=" ")
    print()