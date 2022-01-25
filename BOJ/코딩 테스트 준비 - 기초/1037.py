n=int(input())
x=list(map(int,input().split()))
y=sorted(x)
if n==0:
    print(x[-1])
else:
    if n%2==1:
        print(y[int(n/2)]**2)
    else:
        print(y[0]*y[-1])