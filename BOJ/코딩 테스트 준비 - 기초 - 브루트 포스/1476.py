E,S,M=map(int,input().split())
tem=[0,0,0]
ans=[E,S,M]
cnt=0
while True:
    if tem[0] == 15:
        tem[0] = 1
    else:
        tem[0] += 1
    if tem[1] == 28:
        tem[1] = 1
    else:
        tem[1] += 1
    if tem[2] == 19:
        tem[2] = 1
    else:
        tem[2] += 1
    
    cnt += 1
    
    if tem == ans:
        print(cnt)
        break