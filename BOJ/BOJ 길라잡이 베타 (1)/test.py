def han(num):
    num = str(num)
    if int(num) < 10:
        return 1
    temp = int(num[0]) - int(num[1])
    for i in range(len(num) - 1):
        if int(num[i]) - int(num[i + 1]) != temp:
            return 0
    return 1

N = int(input())
ans = 0
for i in range(1, N + 1):
    if (han(i)):
        ans += 1
print(ans)

