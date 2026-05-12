import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


R, C = minput()
g = []
for _ in range(R):
    tmp = []
    s = input_().rstrip()
    for char in s:
        if char == '.':
            tmp.append(1)
        else:
            tmp.append(0)
    g.append(tmp)

ans = 0
for start in range(R):
    if not g[start][0]:
        continue
    ok = True
    i = start
    seq = [i]
    j = 1
    while j < C:
        if i and g[i - 1][j]:
            seq.append(i - 1)
            i -= 1
            j += 1
        elif g[i][j]:
            seq.append(i)
            j += 1
        elif i != R - 1 and g[i + 1][j]:
            seq.append(i + 1)
            i += 1
            j += 1
        elif seq:
            seq.pop()
            j -= 1
        else:
            ok = False
            break
    if ok:
        for j in range(C):
            g[seq[j]][j] = 0
        ans += 1

print(ans)
