from math import factorial as fac

a,b = map(int,input().split())
ans = fac(a) // (fac(b) * fac(a - b))
print(ans)