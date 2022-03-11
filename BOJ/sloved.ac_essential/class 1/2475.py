cnt = 0
arr = list(map(int, input().split()))
for i in arr:
    cnt += i * i
print(cnt % 10)