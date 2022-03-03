N = int(input())
arr = [0]
dp = [0] * (N + 1)
for _ in range(N):
    arr.append(int(input()))
if N == 1:
    print(arr[1])
    exit()
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]
for i in range(3, N + 1):
    dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i], dp[i - 1])
print(max(dp))