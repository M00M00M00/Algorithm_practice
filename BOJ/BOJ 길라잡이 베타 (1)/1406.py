import sys
s=list(sys.stdin.readline().rstrip())
ss=[]
N=int(sys.stdin.readline())
cursor=len(s)-1
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "P":
        s.append(command[1])
    elif command[0] == 'L':
        if s:
            ss.append(s.pop())
    elif command[0] == 'D':
        if ss:
            s.append(ss.pop())
    elif command[0] == 'B':
        if s:
            s.pop()
print("".join(s+list(reversed(ss))))