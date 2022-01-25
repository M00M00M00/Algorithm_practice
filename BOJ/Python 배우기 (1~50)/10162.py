N=int(input())
a = N//300
N = N % 300
b = N // 60
N = N % 60
c = N // 10
N = N % 10
if N == 0:
    print(a,b,c)
else:
    print(-1)