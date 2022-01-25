N=int(input())
arr=list(map(int,input().split()))
M=int(input())
check=list(map(int,input().split()))
for i in check:
    if i in arr:
        print(1)
    else:
        print(0)