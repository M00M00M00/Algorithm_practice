import sys
from collections import deque

def stack(arr, command):
    if command == 'pop_front':
        if len(arr) != 0:
            print(arr.popleft())
        else:
            print(-1)
    elif command == 'pop_back':
        if len(arr) != 0:
            print(arr.pop())
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
    if command[0] == 'push_front':
        arr.appendleft(command[1])
    elif command[0] == 'push_back':
        arr.append(command[1])
    else:
        stack(arr, command[0])