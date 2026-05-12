from math import isqrt
from algorithms import sieve
from heapq import heappop, heappush


mx = isqrt(1700000000)
primes = sieve(mx)
heap = [(primes[x], 1, x) for x in range(len(primes))]
ans = []
while heap:
    cur, size, idx = heappop(heap)
    ans.append((cur, size))
    for nxt in range(idx + 1, len(primes)):
        if cur * primes[nxt] <= mx:
            heappush(heap, (cur * primes[nxt], size + 1, nxt))

print(ans)
