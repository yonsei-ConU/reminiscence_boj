import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


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


l = list(minput())[::-1]
f = fail(l)
k = p = 9999999999
for i in range(len(l)):
    tk = len(l) - 1 - i
    tp = i - f[i] + 1
    if tk < k or (tk == k and tp < p):
        k = tk
        p = tp

print(k, p)
