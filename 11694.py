import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


lst = ['cubelover', 'koosaga']
N = int(input_())
P = list(minput())
if set(P) == {1}:
    print(lst[(N + 1) % 2])
else:
    ans = 0
    for s in P: ans ^= s
    print(lst[bool(ans)])
