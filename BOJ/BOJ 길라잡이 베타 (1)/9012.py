def isPS(s):
    while True:
        sw=True
        for i in range(len(s)-1):
            if s[i] == '(' and s[i+1] == ')':
                s = s[0:i]+s[i+2:]
                sw=False
                break
        if sw:
            break
    if s:
        print('NO')
    else:
        print('YES')
            

N=int(input())
for _ in range(N):
    s=str(input())
    isPS(s)