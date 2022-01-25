N=int(input())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a1.sort()
a2.sort(reverse=True)
cnt=0
for i in range(N):
    cnt += a1[i] * a2[i]
print(cnt)
