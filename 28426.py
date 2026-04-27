import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def sieve(n):
    a = [False,False] + [True]*(n-1)

    for i in range(2,n+1):
      if a[i]:
        for j in range(2*i, n+1, i):
            a[j] = False
    return a


N = int(input_())
if N == 1: exit(print(696969))
elif N == 2: exit(print('2 4'))
else:
    sum_t = N * (N - 1)
    primes = sieve(1000000)
    for i in range(3, 1000001):
        if primes[i] and not sum_t % i:
            break
    else:
        assert 1 == 2
    ans = list(range(2, 2 * N, 2))
    for element in ans:
        assert element % (sum_t + i)
    ans = list(map(str, ans + [i]))
    print(' '.join(ans))
