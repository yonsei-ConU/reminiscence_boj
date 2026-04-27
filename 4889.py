tc = 1
while True:
    s = input()
    if s[0] == '-':
        break
    cnt = 0
    ans = 0
    for p in s:
        if p == '{':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            ans += 1
            cnt += 2

    print(f"{tc}. {ans + cnt // 2}")
    tc += 1
