N = int(input())

board = [[] for _ in range(3)]

for i in range(N):
    candies = str(input())
    board[i].append(candies)

print(board)