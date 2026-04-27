import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, d = minput()
if N >= sum(i * d**i for i in range(d)):
    print(-1)
    exit()

while True:
    N += 1
    n = N
    digits = []
    while n:
        if n % d in digits:
            break
        digits.append(n % d)
        n //= d
    else:
        if len(digits) == d:
            print(N)
            break
