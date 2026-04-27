import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def mex(s):
    ret = 0
    while ret in s:
        ret += 1
    return ret


def fail(s2):
    ret = [0] * len(s2)
    j = 0
    for i in range(1, len(s2)):
        while j > 0 and s2[i] != s2[j]:
            j = ret[j - 1]

        if s2[i] == s2[j]:
            j += 1
            ret[i] = j
    return ret


M = int(input_())
K = int(input_())
trans = list(minput())
grundy = [0]
for i in range(1, 471937):
    nxt = set()
    for t in trans:
        if i < t:
            continue
        nxt.add(grundy[i - t])
    grundy.append(mex(nxt))

l = grundy[::-1]
f = fail(l)
k = p = 99090909009099009089
for i in range(len(l)):
    tk = len(l) - 1 - i
    tp = i - f[i] + 1
    if tk + tp < k + p or (tk + tp == k + p and tp < p):
        k = tk
        p = tp
assert p < len(grundy) / 2
if M < len(grundy):
    exit(print(grundy[:M + 1].count(0)))
ans = grundy[1:k].count(0)
one_cycle = grundy[k:k + p].count(0)
q, r = divmod(M + 1 - k, p)
print(ans + q * one_cycle + grundy[k:k + r].count(0))
