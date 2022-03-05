def dfs(n, selected, clothes):
    global answer

    if (n >= len(clothes)):
        return

    for j in range(n, len(clothes)):
        sw = 0
        for i in range(j):
            if (selected[i] == 1 and clothes[i][1] == clothes[j][1]):
                dfs(j + 1, selected, clothes)
                sw = 1
                break
        if not sw:
            answer += 1
            selected[j] = 1
            dfs(j + 1, selected, clothes)
            selected[j] = 0


def solution(clothes):
    global answer

    answer = 0
    selected = [0] * len(clothes)
    dfs(0, selected, clothes)
    return answer