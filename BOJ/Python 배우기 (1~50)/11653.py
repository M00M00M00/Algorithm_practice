N=int(input())
cnt=2
while N > 1:
    while N % cnt == 0:
        N = N // cnt
        print(cnt)
    cnt += 1