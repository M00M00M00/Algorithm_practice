arr=[]
N=int(input())
for _ in range(N):
    arr.append(list(map(str,input())))
answer=N*N
cnt=0
while True:
    whole_cnt=0
    for i in range(N):
        cnt_col=0
        for j in range(N):
            if arr[j][i] == 'T':
                cnt_col += 1
        if cnt_col > N//2:
            cnt+=1
            whole_cnt+=1
            for j in range(N):
                if arr[j][i] == 'H':
                    arr[j][i] = 'T'
                else:
                    arr[j][i] = 'H'
    for i in range(N):
        cnt_row=0
        for j in range(N):
            if arr[i][j] == 'T':
                cnt_row += 1
        if cnt_row > N//2:
            cnt+=1
            whole_cnt+=1
            for j in range(N):
                if arr[i][j] == 'H':
                    arr[i][j] = 'T'
                else:
                    arr[i][j] = 'H'
    if whole_cnt == 0:
        break
cnt_t=0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            cnt_t+=1
print(str(cnt_t))
