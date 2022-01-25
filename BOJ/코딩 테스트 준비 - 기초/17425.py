N=int(input())
arr=[1 for _ in range(1000001)]
for i in range(2,1000001):
    for j in range(i,1000000//i * i, i):
        arr[j-1] += i

s=[0 for _ in range(1000001)]

for i in range(1,1000001):
    s[i] = s[i-1] + arr[i]


ans=[]

for _ in range(N):
    x= int(input())
    ans.append(s[x-1])

for i in ans:
    print(i+1)