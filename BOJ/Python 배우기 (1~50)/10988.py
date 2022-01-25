a=str(input())
front=list(a)
back=[]
for i in range(len(a)-1,-1,-1):
    back.append(front[i])
if front == back:
    print(1)
else:
    print(0)