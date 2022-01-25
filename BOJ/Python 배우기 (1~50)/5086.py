def solve(n,m):
    if m % n == 0:
        print('factor')
    elif n % m == 0:
        print('multiple')
    else:
        print('neither')

while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    solve(a,b)