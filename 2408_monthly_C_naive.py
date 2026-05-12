s = input()
ans = set()
for i in range(len(s) + 1):
    for j in range(97, 97 + 26):
        s_temp = s[:i] + chr(j) + s[i:]
        ans.add(s_temp)

print(len(ans))
