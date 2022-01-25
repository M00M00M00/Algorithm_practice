def anyother(h,m,s):
    if (h//24 + m//60 + s//60) > 0:
        return True
    else:
        return False

A,B,C=map(int,input().split())
s=int(input())

C = C + s

while anyother(A,B,C):
    if C //60 > 0:
        B += C // 60
        C = C % 60
    if B // 60 > 0:
        A += B // 60
        B = B % 60
    if A > 23:
        A = A % 24

print(A,B,C)