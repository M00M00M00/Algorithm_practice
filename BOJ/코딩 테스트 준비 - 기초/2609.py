a,b = map(int,input().split())
m_ab=min(a,b)
tmp_1=0
for i in range(1, m_ab+1):
    if a%i==0 and b%i==0:
        tmp_1=max(tmp_1, i)
        
print(tmp_1)

for i in range(1,b+1):
    if (a*i)%b == 0:
        print(a*i)
        break
        
        