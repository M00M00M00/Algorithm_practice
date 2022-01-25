def solve(a,b,c):
    if a > (b - c):
        print('do not advertise')
    elif a < (b - c):
        print('advertise')
    else:
        print('does not matter')

for _ in range(int(input())):
    a,b,c = map(int,input().split())
    solve(a,b,c)