M, N = map(int,input().split())
dict_hear = {}
dict_see = {}
ans = []
for _ in range(M):
    x = str(input())
    dict_hear[x] = 1
for _ in range(N):
    x = str(input())
    dict_see[x] = 1
for i in dict_hear.keys():
    try:
        dict_see[i]
        ans.append(i)
    except:
        continue
ans.sort()
print(len(ans))
for i in ans:
    print(i)
