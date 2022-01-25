N=int(input())
arr=list(map(str,input()))
acnt=0
bcnt=0
for i in arr:
    if i == "A":
        acnt += 1
    else:
        bcnt += 1

if acnt > bcnt:
    print('A')
elif acnt < bcnt:
    print('B')
else:
    print('Tie')