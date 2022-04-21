import sys

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    M = int(input())
    dict = {}
    for _ in range(M):
        value, key = map(str, input().split())
        if key not in dict:
            dict[key] = [value]
        else:
            dict[key].append(value)
    ans = 1
    for i in dict:
        ans *= len(dict[i]) + 1
    ans -= 1
    print(ans)