from heapq import heappush, heappop


def sieve(n):
    a = [False, False] + [True] * (n - 1)
    primes = []
    for i in range(2, n + 1):
        if a[i]:
            heappush(primes, i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return primes


n = int(input())
if n <= 1:
    print(n + 1)
    exit()

heap = sieve(2000000)
r = 1

for i in range(n):
    t = heappop(heap)
    r *= t
    r %= 2000003
    heappush(heap, t**2)

print(r)
