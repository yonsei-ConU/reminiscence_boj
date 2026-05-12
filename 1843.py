import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
# A
print(sum(x // 2 + bool(x % 2) - 1 for x in range(1, N + 1)))
# B
divisors = []
for i in range(1, N + 1):
    if not N % i:
        divisors.append(i)

x = len(divisors)
s = set(divisors)
ans = 0
for i in range(x - 1):
    for j in range(i + 1, x):
        k = divisors[j] - divisors[i]
        if k in s and k <= divisors[i]:
            ans += 1

print(ans)
# C
a = [False, False] + [True] * (N - 1)
primes = []

for i in range(2, N + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, N + 1, i):
            a[j] = False

ans = 0
for i in range(len(primes) - 1):
    if primes[i + 1] - primes[i] == 2:
        ans += 1

print(ans)