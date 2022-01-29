N=int(input())
dis=list(map(int,input().split()))
price=list(map(int,input().split()))

price.pop()

temp=price[0]
cnt=0

for i in range(N-1):
    temp = min(temp,price[i])
    cnt += temp * dis[i]
print(cnt)