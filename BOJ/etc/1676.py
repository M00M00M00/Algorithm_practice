import math
n=int(input())
x=math.factorial(n)
cnt=0
while x % 10 == 0:
    cnt += 1
    x = x//10

print(cnt)