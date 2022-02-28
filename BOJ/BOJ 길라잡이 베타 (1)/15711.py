N = int(input())

n = 4000000
sosu_list = [1] *(n + 1)
sosu_list[0] = 0
sosu_list[1] = 0
for i in range(2 , n + 1):
    if (sosu_list[i]):
        for j in range(2 * i, n+ 1 , i):
            sosu_list[j] = 0

so = []
for i in range(len(sosu_list)):
    if (sosu_list[i]):
        so.append(i)


def is_prime(n):
    for i in range(len(so)):
        if so[i] * so[i] > n:
            break 
        if (n % so[i]) == 0:
            return (0)
    return (1)

for i in range(N):
    a,b = map(int, input().split())
    X = (a + b)
    if (X < 4):
        print ("NO")
    elif (X % 2 == 0):
        print("YES")
    else: #N is even num
        if (is_prime(X - 2)):
            print ("YES")
        else:
            print ("NO")