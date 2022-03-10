import heapq
import sys

q = []
N = int(input())
dict = {}
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(q) == 0:
            print("0")
        else:
            if dict.get(q[0]) == None:
                print(heapq.heappop(q))
            else:
                if dict[q[0]] == 0:
                    print(heapq.heappop(q))
                else:
                    dict[q[0]] -= 1
                    print(-heapq.heappop(q))
    else:
        if x < 0:
            if dict.get(abs(x)) == None:
                dict[abs(x)] = 1
            else:
                dict[abs(x)] += 1
        heapq.heappush(q, abs(x))