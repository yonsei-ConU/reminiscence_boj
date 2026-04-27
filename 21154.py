import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def matrix_mult(a, b):
    mod = 37
    r = [[0] * len(b[0]) for _ in range(len(a))]
    for p in range(len(a)):
        for q in range(len(b[0])):
            for s in range(len(a[0])):
                r[p][q] += a[p][s] * b[s][q]
            r[p][q] %= mod
    return r


n = int(input_())
enc = [list(minput()) for _ in range(n)]
txt = input_().rstrip()
ptr = 0
res = ''
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
while ptr < len(txt):
    segment = txt[ptr:ptr+n]
    vector = []
    for i in range(n):
        if i >= len(segment):
            t = ' '
        else:
            t = segment[i]
        t = ord(t)
        if t == 32:
            vector.append([36])
        elif t < 60:
            vector.append([t - 48 + 26])
        else:
            vector.append([t - 65])
    mult = matrix_mult(enc, vector)
    for i in mult:
        res += characters[i[0]]
    ptr += n

print(res)
