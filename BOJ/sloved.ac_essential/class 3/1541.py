s = list(map(str, input().split('-')))
for i in range(len(s)):
    s[i] = list(map(int, s[i].split('+')))
    s[i] = sum(s[i])
ans = 2 * s[0]
for i in range(len(s)):
    ans -= s[i]
print(ans)