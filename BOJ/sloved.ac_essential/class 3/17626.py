N = int(input())
MAX = N
arr = [0] * (MAX + 1)
arr[0] = 0
arr[1] = 1

for i in range(2, (MAX + 1)):
    temp = MAX
    j = 1
    while (j ** 2) <= i:
        temp = min(temp, arr[i - j ** 2] + 1)
        j += 1
    arr[i] = temp
print(arr[N])