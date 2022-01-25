def allin(arr,N):
    for i in str(N):
        if int(i) not in arr:
            return False
    return True

target=int(input())
N=int(input())
if N != 0:
    broken=list(map(int,input().split()))
else:
    broken=[]
arr=[i for i in range(10)]
for i in broken:
    arr.remove(i)

if N == 10:
    print(abs(100-target))
elif arr == [0]:
    print(min(abs(100-target), 1 + abs(target)))
elif target == 0:
    cnt1=0
    temp1=0
    while True:
        if allin(arr,temp1):
            break
        else:
            temp1 += 1
            cnt1 += 1
    ans = len(str(temp1)) + abs(target - temp1)
    ans = min(ans, abs(100 - target))
    print(ans)
else:
    cnt1=0
    cnt2=0
    temp1=target
    temp2=target
    while True:
        if allin(arr,temp1):
            break
        else:
            temp1 += 1
            cnt1 += 1

    sw=True
    while temp2>0:
        if allin(arr,temp2):
            sw=False
            break
        else:
            temp2 -= 1
            cnt2 += 1
    if sw:
        ans = len(str(temp1)) + abs(target - temp1)
        ans = min(ans, abs(100 - target))
    else:
        if cnt1 + len(str(temp1)) > cnt2 + len(str(temp2)):
            temp = temp2
        else:
            temp = temp1
        
        ans = len(str(temp)) + abs(target - temp)
        ans = min(ans, abs(100 - target))
    print(ans)