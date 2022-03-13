


from collections import deque


while (1):
    s = str(input())
    if s == ".":
        exit()
    arr = deque([])
    sw = 0
    for i in s:
        if i == "[" or i == "(":
            arr.append(i)
        elif i == "]":
            if (arr):
                if arr[-1] != "[" :
                    print("no")
                    sw = 1
                    break
                else:
                    arr.pop()
            else:
                print("no")
                sw = 1
                break
        elif i == ")":
            if arr:
                if arr[-1] != "(":
                    print("no")
                    sw = 1
                    break
                else:
                    arr.pop()
            else:
                print("no")
                sw = 1
                break
    if sw == 0:
        if arr:
            print("no")
        else:
            print("yes")