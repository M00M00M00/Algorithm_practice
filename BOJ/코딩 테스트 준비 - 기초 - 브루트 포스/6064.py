def sol(N, M, x, y):
    while x <= N * M:
        if (x - y) % M == 0:
            return x
        x += N
    return -1 

for _ in range(int(input())):
    N,M,x,y=map(int,input().split())
    print(sol(N,M,x,y))