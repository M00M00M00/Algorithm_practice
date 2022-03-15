from string import ascii_lowercase

dict = {}
for i in range(26):
    dict[ascii_lowercase[i]] = i + 1
ans = 0
N = int(input())
s = str(input())
for i in range(len(s)):
    ans += dict[s[i]] * (31 ** i)
print(ans % 1234567891)