def solve(n):
    cnt=0
    arr=[]
    for i in range(1,n):
        if n % i == 0:
            cnt += i
            arr.append(i)
    if cnt == n:
        new=" + ".join(map(str,arr))
        print(n,"=",new)
    else:
        print(n,"is NOT perfect.")

while True:
    x=int(input())
    if x == -1:
        break
    else:
        solve(x)