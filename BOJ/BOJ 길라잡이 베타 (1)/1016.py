m, M = map(int, input().split())
arr = [1] * (M - m + 1)
i = 2
while (i * i <= M):
    if (m % (i * i) == 0):
        x = m // (i * i)
    else:
        x = m // (i * i) + 1
    for j in range(x * (i * i), M + 1, i * i):
        arr[j - m] = 0
    i += 1
print(sum(arr))