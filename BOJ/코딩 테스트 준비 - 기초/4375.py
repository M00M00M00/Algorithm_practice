while True:
    try:
        n= int(input())
        num=1
        count=1
    except EOFError:
        break
    if n==1:
        print('1')
        continue
    while True:
        num=num*10+1
        count+=1
        if (num%n)==0:
            print(count)
            break