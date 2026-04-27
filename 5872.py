s = input()
cnt = 0
ans = 0
for p in s:
    if p == '(':
        cnt += 1
    else:
        cnt -= 1
    if cnt < 0:
        ans += 1
        cnt += 2

print(ans + cnt // 2)
