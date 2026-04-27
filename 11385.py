import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def fft(arr, mod, root, inverse=False):
    n = len(arr)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while not (j := j ^ bit) & bit:
            bit >>= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    length = 2
    while length <= n:
        omega = pow(root, (mod - 1) // length, mod)
        if inverse:
            omega = pow(omega, -1, mod)
        for i in range(0, n, length):
            w = 1
            for j in range(length // 2):
                u = arr[i + j]
                v = arr[i + j + length // 2] * w % mod
                arr[i + j] = (u + v) % mod
                arr[i + j + length // 2] = (u - v) % mod
                w = w * omega % mod
        length *= 2

    if inverse:
        inv_n = pow(n, -1, mod)
        arr = [(x * inv_n) % mod for x in arr]
    return arr


def conv(a, b, mod, root):
    n = len(a) + len(b) - 1
    size = 1
    while size < n:
        size <<= 1
    a.extend([0] * (size - len(a)))
    b.extend([0] * (size - len(b)))
    a = fft(a, mod, root)
    b = fft(b, mod, root)
    c = [(a[i] * b[i]) % mod for i in range(size)]
    c = fft(c, mod, root, True)
    return c[:n]


def crt(mods, remainders):
    x = 1
    for m in mods:
        x *= m
    ret = 0
    for m, r in zip(mods, remainders):
        t = x // m
        ret += r * t * pow(t, -1, m)

    return ret % x


N, M = minput()
f = list(minput())
g = list(minput())
result1 = conv(f[:], g[:], 29686813949953, 5)
result2 = conv(f, g, 4123168604161, 7)
ans = 0
for i in range(len(result1)):
    ans ^= crt([29686813949953, 4123168604161], [result1[i], result2[i]])
print(ans)
