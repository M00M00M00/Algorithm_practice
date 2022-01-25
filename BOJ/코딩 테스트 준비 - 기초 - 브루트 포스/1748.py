N=int(input())
x=len(str(N))
cnt=0
for i in range(1,x):
    cnt += 9*(10**(i-1)) * i

cnt += (N - (10**(x-1) - 1))*x

print(cnt)