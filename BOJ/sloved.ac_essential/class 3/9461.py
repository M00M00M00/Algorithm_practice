arr = [0, 1, 1, 1, 2, 2]
for i in range(len(arr), 101):
    arr.append(arr[i - 1] + arr[i - 5])
N = int(input())
for _ in range(N):
    i = int(input())
    print(arr[i])