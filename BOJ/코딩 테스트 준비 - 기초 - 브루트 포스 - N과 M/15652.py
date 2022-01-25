import itertools
N,M=map(int,input().split())
a=itertools.combinations_with_replacement(range(1,N+1),M)
for i in a:
    for j in i:
        print(j,end=" ")
    print()