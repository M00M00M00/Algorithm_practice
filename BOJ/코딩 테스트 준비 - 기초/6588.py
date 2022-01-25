import math
arr = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        arr.append(x)

sosu = [True for _ in range(1000001)]
for i in range(2, 1001):
    if sosu[i]:
        for j in range(2 * i, 1000001, i):
            sosu[j] = False

for i in arr:
    cnt = 0
    for j in range(3,len(sosu)):
        if sosu[j] and sosu[i-j]:
            print(i, "=", j, "+", i-j)
            cnt += 1
            break
    if cnt == 0:
        print("Goldbach's conjecture is wrong.")
