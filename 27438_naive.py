# r번째에서 시작, t부터

r = 0
t = 666
ans = []
while r <= 13559699:
    if '666' in str(t):
        r += 1
        if not r % 1000:
            ans.append(t)
        if not r % 100000:
            print(r)
    t += 1

print(ans)
