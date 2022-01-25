import copy


def check(lst):
    ans_r = 1
    for i in range(len(lst)):
        tem = 1
        for j in range(len(lst) - 1):
            if lst[i][j] == lst[i][j + 1]:
                tem += 1
            else:
                tem = 1
            ans_r = max(tem, ans_r)
            if tem == len(lst):
                return len(lst)
    ans_c = 1
    for i in range(len(lst)):
        tem = 1
        for j in range(len(lst) - 1):
            if lst[j][i] == lst[j + 1][i]:
                tem += 1
            else:
                tem = 1
            ans_c = max(tem, ans_c)
            if tem == len(lst):
                return len(lst)
    return max(ans_c, ans_r)


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(str, input())))
ans = 0
for i in range(N):
    for j in range(N - 1):
        tem = copy.deepcopy(arr)
        if tem[i][j] != tem[i][j + 1]:
            tem[i][j], tem[i][j + 1] = tem[i][j + 1], tem[i][j]
            ans = max(ans, check(tem))
            if ans == N:
                break

for i in range(N):
    for j in range(N - 1):
        tem = copy.deepcopy(arr)
        if tem[j][i] != tem[j + 1][i]:
            tem[j][i], tem[j + 1][i] = tem[j + 1][i], tem[j][i]
            ans = max(ans, check(tem))
            if ans == N:
                break

print(ans)
