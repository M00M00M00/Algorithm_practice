import heapq
def solution(jobs):
    arr=[]
    N=len(jobs)
    cnt=0
    for i in jobs:
        arr.append(i[1])
    heapq.heapify(arr)
    for i in range(N):
        temp=heapq.heappop(arr)
        
    answer = cnt/N
    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))