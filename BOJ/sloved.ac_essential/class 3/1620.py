M, N = map(int,input().split())
dict_name = {}
dict_number = {}
for i in range(1, M + 1):
    name = str(input())
    dict_name[name] = str(i)
    dict_number[str(i)] = name
for _ in range(N):
    x = str(input())
    if x in dict_name:
        print(dict_name[x])
    else:
        print(dict_number[x])
