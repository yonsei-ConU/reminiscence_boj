import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
good = []
bad = []
for _ in range(N):
    a, b = minput()
    if a <= b:
        good.append((a, b))
    else:
        bad.append((a, b))

cur = 0
good.sort()
for cost, benefit in good:
    if cost > cur:
        exit(print(0))
    cur -= cost
    cur += benefit

bad.sort(key=lambda x: -x[1])
for cost, benefit in bad:
    if cost > cur:
        exit(print(0))
    cur -= cost
    cur += benefit

print(1)
