def check(rownum):
    global cnt
    if rownum == n:
        cnt+=1
        return
    for i in range(n):
        sw=True
        for j in range(rownum):
            if arr[j] == i or (rownum - j) == abs(arr[j] - i):
                sw=False
                break
        if sw:
            arr[rownum] = i 
            check(rownum+1)


n = int(input())
cnt=0
arr=[0]*n
check(0)

print(cnt)