import itertools

def ok(x,y):
    arr=[[x[0]-1,x[1]],[x[0]+1,x[1]],
         [x[0],x[1]-1],[x[0],x[1]+1]]
    if y in arr:
        return False
    else:
        return True
    
def maxarr(arr,n):
    lst=[]
    for i in arr:
        for j in i:
            lst.append(j)
    lst.sort(reverse=True)
    return sum(lst[:n])
    
N,M,K=map(int,input().split())
arr=[]
new_arr=[]
tablet=[]
for _ in range(N):
   tablet.append(list(map(int,input().split()))) 
for i in range(N):
    for j in range(M):
        arr.append([i,j])
a=itertools.combinations(arr,K)

ans=-10000*K
m_n=maxarr(tablet,K)

for i in a:
    temp=0
    for j in range(K):
        temp += tablet[i[j][0]][i[j][1]]
    if temp > ans:
        b=itertools.combinations(i,2)
        sw=True
        for j in b:
            if not ok(j[0],j[1]):
                sw=False
                break
        if sw==True:
            ans=temp
    if ans == m_n:
        break

print(ans)