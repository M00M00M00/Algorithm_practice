n=int(input())
t=[0]
p=[0]
d=[0]*(n+2)
for _ in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)

for i in range(1,n+2):
    for j in range(1,i):
        d[i] = max(d[i], d[j])

        if i == j + t[j]:
            d[i] = max(d[i], d[j] + p[j])

print(d[-1])