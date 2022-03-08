def check(arr_list, num):
    global arr

    lst_len = len(arr_list)
    if lst_len == 0:
        return 1
    if arr[lst_len - 1] == '>':
        if arr_list[-1] <= num:
            return 0
    elif arr[lst_len - 1] == '<':
        if arr_list[-1] >= num:
            return 0
    return 1


def dfs(N, n):
    global mmax
    global mmin
    global selected
    global arr_list

    if n == N + 1:
        ans = ''.join(map(str,arr_list))
        mmax = max(mmax, int(ans))
        mmin = min(mmin, int(ans))
        return
    for i in range(10):
        if selected[i] == 0 and check(arr_list, i) == 1:
            selected[i] = 1
            arr_list.append(i)
            dfs(N, n + 1)
            selected[i] = 0
            arr_list.remove(i)

def solution(N):
    global mmax
    global mmin
    global selected
    global arr_list
    global arr

    mmax = 0
    mmin = 9999999999
    arr = list(map(str, input().split()))
    arr_list = []
    selected = [0] * 10
    dfs(N, 0)
    if len(str(mmax)) != N + 1:
        print('0' + str(mmax))
    else:
        print(str(mmax))
    if len(str(mmin)) != N + 1:
        print('0' + str(mmin))
    else:
        print(str(mmin))
N = int(input())
solution(N)