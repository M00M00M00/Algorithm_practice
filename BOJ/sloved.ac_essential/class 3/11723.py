import sys
from collections import deque
input= sys.stdin.readline
N = int(input())
ans = deque([])
for _ in range(N):
    x = list(map(str,input().split()))
    if x[0] == "add":
        if x[1] not in ans:
            ans.append(x[1])
    elif x[0] == "remove":
        try:
            ans.remove(x[1])
        except:
            continue
    elif x[0] == "check":
        if x[1] in ans:
            print("1")
        else:
            print("0")
    elif x[0] == "toggle":
        if x[1] in ans:
            ans.remove(x[1])
        else:
            ans.append(x[1])
    elif x[0] == "all":
        ans = list(map(str, range(1, 21)))
    elif x[0] == "empty":
        ans = []
    else:
        print("error")
