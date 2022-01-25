import itertools
N,M=map(int,input().split())
a=itertools.permutations(range(1,N+1),M)
for i in a:
    for j in i:
        print(j,end=" ")
    print()