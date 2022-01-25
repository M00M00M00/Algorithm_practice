N,M=map(int,input().split())
m=int(input())

if M + m >= 60:
    N += (M + m)//60
    if N >= 24:
        N = N % 24
    M = (M + m) % 60
else:
    M = M + m
print(N,M)