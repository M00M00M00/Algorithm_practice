import sys
from collections import deque

def stack(arr, command):
    if command == 'top':
        if len(arr) != 0:
            print(arr[-1])
        else:
            print(-1)
    elif command == 'pop':
        if len(arr) != 0:
            print(arr.popleft())
        else:
            print(-1)
    elif command == 'size':
        print(len(arr))
    elif command == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif command == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])

N=int(sys.stdin.readline())
arr=deque([])
for _ in range(N):
    command= sys.stdin.readline().split()
    if command[0] == 'push':
        arr.append(command[1])
    else:
        stack(arr, command[0])