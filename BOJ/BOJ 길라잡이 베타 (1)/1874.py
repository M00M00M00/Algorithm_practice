N=int(input())
arr=list(range(N,0,-1))
s=[]
new=[]
result=[]
for _ in range(N):
    s.append(int(input()))

for i in s:
    while True:
        if new:
            if new[-1] == i:
                    new.pop()
                    result.append('-')
                    break
            elif arr:
                if arr[-1] <= i:
                    new.append(arr.pop())
                    result.append('+')
                else:
                    print("NO")
                    exit()
            else:
                print("NO")
                exit()
        else:
            new.append(arr.pop())
            result.append('+')

for i in result:
    print(i)