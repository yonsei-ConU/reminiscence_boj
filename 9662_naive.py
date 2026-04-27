from random import sample, randint

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


mM = []
notmM = []
inf = []
for i in range(50):
    trans = sample(range(1, 23), randint(3, 6))
    grundy = [0]
    ans = []
    for i in range(1, 100001):
        nxt = set()
        for t in trans:
            if i - t < 0:
                continue
            nxt.add(grundy[i - t])
        grundy.append(mex(nxt))

    l = grundy[::-1]
    f = fail(l)
    k = p = 999999999999999999999
    for i in range(len(l)):
        tk = len(l) - 1 - i
        tp = i - f[i] + 1
        if tk + tp < k + p or (tk + tp == k + p and tp < p):
            k = tk
            p = tp

    if p < len(grundy) / 2:
        s = f"{', '.join(map(str, sorted(trans)))} -> {k}, {p}"
        if max(trans) + min(trans) == p:
            mM.append(s)
        else:
            notmM.append(s)
    else:
        s = f"{', '.join(map(str, sorted(trans)))} -> 50000+"
        inf.append((s, grundy[:200]))

print("*****Max + min*****")
for v in mM:
    print(v)
print("*****   WTF   *****")
for v in notmM:
    print(v)
print("*****   INF   *****")
for v in inf:
    print(v[0])
    print(v[1])
