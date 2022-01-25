def solution(P):
    ans = []
    pos_ans=[]
    if len(P)==2:
        if can_pellindrom(P[0],P[1]):
            ans.append(P[1])
    else:
        for i in range(1,len(P)):
            a1=P[0]+P[i]
            a2=P[i]+P[0]
            if pellindrom(a1) or pellindrom(a2):
                pos_ans.append(P[i])
        
        for i in pos_ans:
            arr_check=P[:]
            arr_check.remove(P[0])
            arr_check.remove(i)
            if check_arr(arr_check):
                ans.append(i)
    return ans

def pellindrom(N):
    ans=True
    for i in range(len(N)):
        if N[i] != N[len(N)-1-i]:
            ans=False
    return ans

def can_pellindrom(a1,a2):
    x1=a1+a2
    x2=a2+a1
    if pellindrom(x1) or pellindrom(x2):
        return True
    else:
        return False

def check_arr(lst):
    if len(lst) == 2:
        if can_pellindrom(lst[0], lst[1]):
            return True
        else:
            return False
    else:
        for i in range(1,len(lst)):
            check_num=0
            if can_pellindrom(lst[0],lst[i]):
                lst.remove(lst[0])
                lst.remove(lst[i])
                break
            else:
                check_num+=1
        if check_num == len(lst)-1:
            return False
        else:
            return check_arr(lst)
    
            
solution(["11","1"])