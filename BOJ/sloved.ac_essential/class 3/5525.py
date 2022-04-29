import sys
input = sys.stdin.readline
N = int(input())
find_s = ''.join(["I" if x % 2 == 0 else "O" for x in range(2 * N + 1)])
l = int(input())
s = str(input())
pi = [0] +list(range(2 * N))
i = 0
cnt = 0
j = 0
while (i) < l:
    while j != 0 and s[i] != find_s[j]:
        j = pi[j - 1]
    if s[i] == find_s[j]:
        if (j == 2 * N):
            cnt += 1
            j = pi[j]
        else:
            j += 1
    i += 1 
print(cnt)