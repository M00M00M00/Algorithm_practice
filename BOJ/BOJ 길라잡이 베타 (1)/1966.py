from collections import deque

K = int(input())
for _ in range(K):
    N, M = map(int,input().split())
    arr=deque(list(map(int,input().split())))
    check=deque([0]*N)
    check[M]="target"
    cnt=0
    while True:
        if check[0] == "target":
            if arr[0] == max(arr):
                arr.popleft()
                check.popleft()
                cnt+=1
                break
            else:
                arr.append(arr.popleft())
                check.append(check.popleft())
        else:
            if arr[0] == max(arr):
                arr.popleft()
                check.popleft()
                cnt+=1
            else:
                arr.append(arr.popleft())
                check.append(check.popleft())
    print(cnt)