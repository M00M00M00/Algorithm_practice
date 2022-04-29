import itertools

x = [1,2,3,4,5]
for i in itertools.permutations(x, 3):
    print(i)