from collections import deque
import sys
T=int(sys.stdin.readline())
for _ in range(T):
    command=list(map(str,sys.stdin.readline().rstrip()))
    n=int(sys.stdin.readline())
    ls=str(sys.stdin.readline().rstrip())
    if ls == "[]":
        ls=deque([])
    else:
        ls=deque(list(map(str,ls[1:len(ls)-1].split(","))))
    sw=True
    r_c=0
    for i in command:
        if i == "R":
            r_c += 1
        elif i == "D":
            if ls:
                if r_c % 2 == 0:
                    ls.popleft()
                else:
                    ls.pop()
            else:
                print("error")
                sw=False
                break
    if r_c % 2 == 1:
        ls.reverse()
    answer=""
    if sw:
        print("["+",".join(ls)+"]")