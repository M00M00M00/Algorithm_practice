def dice(a,b,c):
    if a==b and b==c:
        return (10000 + a*1000)
    elif a==b:
        return (1000 + a*100)
    elif b==c:
        return (1000 + b*100)
    elif c==a:
        return (1000 + a*100)
    else:
        return (max(a,b,c)*100)

temp=0

for _ in range(int(input())):
    a,b,c=map(int,input().split())
    temp=max(temp,dice(a,b,c))
print(temp)