import heapq
import sys

q = []
N = int(input())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(q) == 0:
            print("0")
        else:
            print(-1 * heapq.heappop(q))
    else:
        heapq.heappush(q, -x)