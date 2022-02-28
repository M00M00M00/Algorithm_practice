N = int(input())
sosu = range(N + 1)
selected = [1 for _ in range(N + 1)]
cnt = 0

for i in range(2, N + 1):
    if (selected[i]):
        j = i * 2
        while (j <= N):
            selected[j] = 0
            j += i

selected[0] = 0
selected[1] = 0

for i, v in enumerate(selected):
    ans = 0
    if (v):
        for j in range(i, N + 1):
            if (selected[j]):
                ans += j
            if (ans == N):
                cnt += 1
                break ;
            elif (ans > N):
                break ;

print(cnt)
