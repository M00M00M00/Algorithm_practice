import itertools
from math import sqrt

def is_sosu(n):
    if n < 2:
        return (0)
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return (0)
    return (1)

arr = []
numbers=input()
for i in range(1, len(numbers) + 1):
    for j in itertools.permutations(numbers, i):
        ans = 0
        for k in range(len(j)):
            ans = ans * 10 + int((j[k]))
        arr.append(ans)
arr = set(arr)
answer = 0
for i in arr:
    if is_sosu(i):
        answer += 1
print(answer)
