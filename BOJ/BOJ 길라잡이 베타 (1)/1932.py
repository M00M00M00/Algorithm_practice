N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

arr2 = [[0 for _ in range(N)] for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr2[i][j] = arr[i][j]

for i in range(N):
    dp[0][i] = arr2[0][i]

for i in range(1, N):
    for j in range(N):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + arr2[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][i - 1] + arr2[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + arr2[i][j]

print(max(dp[N - 1]))