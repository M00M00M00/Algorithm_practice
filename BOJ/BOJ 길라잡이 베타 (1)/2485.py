N = int(input())
arr=[]
for _ in range(N):
    arr.append(int(input()))
check=[]
for i in range(N-1):
    check.append(arr[i+1]-arr[i])

for i in range(min(check),0,-1):
    sw=True
    for j in check:
        if j%i != 0:
            sw=False
            break
    if sw:
        max_di=i
        break
ans=(arr[-1]-arr[0])//max_di - N + 1
print(ans)