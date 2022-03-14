from collections import deque


N = int(input())
q = deque([])
for _ in range(N):
    x = int(input())
    if x == 0:
        q.pop()
    else:
        q.append(x)
print(sum(q))