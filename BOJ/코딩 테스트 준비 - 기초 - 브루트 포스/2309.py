import itertools
arr=[]
for _ in range(9):
    arr.append(int(input()))
com=itertools.combinations(arr,7)
for i in com:
    if sum(i) == 100:
        ans=sorted(i)
        for j in ans:
            print(j)
        break