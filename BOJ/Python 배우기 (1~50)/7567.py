arr = list(str(input()))
cnt = 10
for i in range(0, len(arr)-1):
    if arr[i] == arr[i+1]:
        cnt += 5
    else:
        cnt += 10
print(cnt)
