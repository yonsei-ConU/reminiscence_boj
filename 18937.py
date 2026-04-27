import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
P = list(minput())
first = input_().rstrip() == 'Whiteking'
ans = 0
for g in P:
    ans ^= g - 2

print(['Whiteking', 'Blackking'][(bool(ans) + first) % 2])
