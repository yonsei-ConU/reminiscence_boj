import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


mod = 998244353
root = 3

def fft(arr, inverse=False):
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

def conv(a, b):
    n = len(a) + len(b) - 1
    size = 1
    while size < n:
        size <<= 1
    a.extend([0] * (size - len(a)))
    b.extend([0] * (size - len(b)))
    a = fft(a)
    b = fft(b)
    c = [(a[i] * b[i]) % mod for i in range(size)]
    c = fft(c, True)
    return c[:n]


def sieve(n):
    a = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if a[i]:
            for j in range(i * i, n + 1, i):
                a[j] = False
    return a


primes = sieve(1000000)
primes2 = [0] * 1000001
for p in range(500001):
    if primes[p]:
        primes2[2 * p] = 1
res = conv(primes, primes2)

for _ in range(int(input_())):
    print(res[int(input_())])
