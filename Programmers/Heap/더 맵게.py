import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) < 2:
            if scoville[0] > K:
                break
            else:
                answer = -1
                break
        else:
            if scoville[0] < K:
                heapq.heappush(scoville, change_num(scoville))
                answer+=1
            else:
                break
    return answer

def change_num(arr):
    first=heapq.heappop(arr)
    second=heapq.heappop(arr)
    return int(first+2*second)