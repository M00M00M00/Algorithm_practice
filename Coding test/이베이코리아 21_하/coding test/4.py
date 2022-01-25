def solution(n, k, bulbs):
    bulbs=list(map(str,bulbs))
    check_list=[]
    cnt=0
    cnt_1=0
    while not check_ans(bulbs):
        cnt_1+=1
        if cnt_1>10:
            return -1
        else:
            for i in range(len(bulbs)-k):
                if bulbs[i] != "R":
                    change_color(bulbs,i,k)
                    check_list.append(bulbs)
                    cnt+=1
    answer = cnt
    return answer


def change_color(bulbs,index,n):
    for i in range(n):
        if bulbs[index+i] == "R":
            bulbs[index+i] = "G"
        elif bulbs[index+i] == "G":
            bulbs[index+i] = "B"
        else:
            bulbs[index+i] = "R"
    return bulbs
            
def check_ans(arr):
    check=True
    for i in arr:
        if i != "R":
            check=False
    return check

print(solution(6,3,"RBGRGB"))