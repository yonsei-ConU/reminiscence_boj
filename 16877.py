import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


MAX = 3000000
N = int(input_())
P = list(minput())
fib = [1, 2]
while fib[-1] <= MAX:
    fib.append(fib[-1] + fib[-2])

grundy = [0, 1]
for i in range(2, MAX + 1):
    next_state = set()
    for f in fib:
        if f > i:
            break
        next_state.add(grundy[i - f])
    mex = 0
    while mex in next_state:
        mex += 1
    grundy.append(mex)

ans = 0
for p in P:
    ans ^= grundy[p]

print(['cubelover', 'koosaga'][bool(ans)])
