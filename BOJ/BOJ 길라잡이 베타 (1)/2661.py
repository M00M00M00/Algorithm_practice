def isGood(s):
    if len(s) == 1:
        return True

    for i in range(1,len(s)//2 + 1):
        for j in range(0, len(s)-i*2+1):
            temp=s[j:j+i]
            if s[j+i:j+2*i] == temp:
                return False
            else:
                temp=s[j+i:j+2*i]
    return True

def dfs(s):
    if len(s) == N:
        if isGood(s):
            print(s)
            exit()
            return

    if isGood(s+"1"):
        dfs(s+"1")
    if isGood(s+"2"):
        dfs(s+"2")
    if isGood(s+"3"):
        dfs(s+"3")
    

N=int(input())
ans='1'
if N == 1:
    print(ans)
else:
    dfs("")
