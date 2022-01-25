n=int(input())
a=0
N=0

while True:
    N+=10**a
    if N%n==0:
        print(len(str(N)))
        break
    else:
        a+=1