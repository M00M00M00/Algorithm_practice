import sys

input = sys.stdin.readline

c, r = map(int,input().split())
table = []
for _ in range(r):
    table.append(list(map(int,input().split())))
print(table)  