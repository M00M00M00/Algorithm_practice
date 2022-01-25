for _ in range(int(input())):
    x=0
    y=0
    for _ in range(9):
        a,b=map(int,input().split())
        x += a
        y += b
    if x > y:
        print('Yonsei')
    elif x < y:
        print('Korea')
    else:
        print('Draw')