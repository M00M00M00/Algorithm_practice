from collections import deque
def find_top_index(board, line):
    for i in range(len(board)):
        if board[i][line - 1] != 0:
            return i
    return -1

def is_last_same(q):
    len_q = len(q)
    if len(q) < 2:
        return False
    else:
        if q[len_q - 1] == q[len_q - 2]:
            return True
        return False

def solution(board, moves):
    answer = 0
    baguni = deque([])
    for i in moves:
        top_idx = find_top_index(board, i)
        if top_idx != -1:
            baguni.append(board[top_idx][i - 1])
            board[top_idx][i - 1] = 0
            while baguni and is_last_same(baguni):
                baguni.pop()
                baguni.pop()
                answer += 2
    return answer