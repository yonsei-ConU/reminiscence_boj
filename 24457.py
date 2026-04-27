import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
E = list(minput())
C = list(minput())
A = [(E[i], C[i]) for i in range(N)]
A.sort(key=lambda x: x[0] - x[1])
ans = 0
S = 0
for e, c in A:
    ans += max(0, e - S)
    S += c

print(ans)
