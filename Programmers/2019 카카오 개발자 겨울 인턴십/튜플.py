def solution(s):
    answer = []
    n_s = list(s[2:len(s) - 2].split("},{"))
    for i in range(len(n_s)):
        n_s[i] = list(map(int,n_s[i].split(',')))
    for i in range(len(n_s)):
        for j in n_s:
            if len(j) == i + 1:
                for k in j:
                    if k not in answer:
                        answer.append(k)
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))