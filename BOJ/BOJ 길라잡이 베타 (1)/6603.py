import itertools

while True:
    c=list(map(int,input().split()))
    if c[0] == 0:
        exit()
    c = c[1:]
    for i in itertools.combinations(c,6):
        print(" ".join(map(str,list(i))))
    print()