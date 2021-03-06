N = int(input())
arr = [0] + list(map(int,input().split()))
dp = [0] * (N + 1)
dp[1] = arr[1]
dp[2] = max(arr[1] * 2, arr[2])
for i in range(3, N + 1):
    dp[i] = arr[i]
    for j in range(1, i // 2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i - j])
print(dp[N])
