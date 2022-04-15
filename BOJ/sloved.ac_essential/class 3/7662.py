import heapq
import sys

input = sys.stdin.readline
for T in range(int(input())):
    min_h = []
    max_h = []
    is_in = [False] * 1000001
    for i in range(int(input())):
        a, b = map(str, input().split())
        b = int(b)
        if a == "I":
            heapq.heappush(min_h, (b, i))
            heapq.heappush(max_h, (-b, i))
            is_in[i] = True
        else:
            if b == 1:
                while max_h and not is_in[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    is_in[max_h[0][1]] = False
                    heapq.heappop(max_h)
            else:
                while min_h and not is_in[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    is_in[min_h[0][1]] = False
                    heapq.heappop(min_h)
    while max_h and not is_in[max_h[0][1]]:
        heapq.heappop(max_h)
    while min_h and not is_in[min_h[0][1]]:
        heapq.heappop(min_h)
    if max_h and min_h:
        print(-max_h[0][0], min_h[0][0])
    else:
        print("EMPTY")