while(1):
    x = int(input())
    if x == 0:
        exit()
    x = str(x)
    l_x = len(x)
    sw = 0
    for i in range(len(x) // 2):
        if x[i] != x[l_x - i - 1]:
            sw = 1
    if sw == 0:
        print("yes")
    else:
        print("no")