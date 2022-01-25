def solution(stones, k):
    answer = ''
    if not pos_stone(stones):
        answer = '-1'
        
        # while sum(stones)>k:
        #     for i in range(len(stones)-1,-1,-1):
        #         if stones[i] == min(stones):
        #             choose(stones, i)
        #             answer_list.append(i)
        #             break
    else:
        answer_list=[]
        main_index=sel_index(stones)
        for _ in range((sum(stones)-k)//4):
            if stones.index(min(stones)) == main_index:
                choose(stones,stones.index(min(stones)))
            elif 
        answer="".join(map(str,answer_list))
    return answer

def pos_stone(arr):
    even_num=0
    odd_num=0
    for i in arr:
        if i%2 == 0:
            odd_num+=1
        else:
            even_num+=1
    if odd_num == 1 or even_num == 1:
        return True
    else:
        return False

def choose(arr,index):
    for i in range(len(arr)):
        arr[i]-=1
    arr[index] += 2
    
def sel_index(arr):
    even_num=0
    odd_num=0
    for i in arr:
        if i%2 == 0:
            odd_num+=1
        else:
            even_num+=1
    if odd_num == 1:
        for i in range(len(arr)):
            if arr[i]%2==0:
                return i
    else:
        for i in range(len(arr)):
            if arr[i]%2==1:
                return i
            
def check_answer(arr,index,k):
    check_lst=[0 for _ in range(len(arr))]
    check_lst[index] = k
    if check_lst == arr:
        return True
    else:
        return False
    
def sel_minindex(arr):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == min(arr):
            return i

print(sel_minindex([4, 2, 2, 1, 4]))