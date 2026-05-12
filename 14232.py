import sys
from algorithms import pollard_rho
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


k = int(input_())
ans = []
while k > 1:
    p = pollard_rho(k)
    ans.append(p)
    k //= p

print(len(ans))
print(*sorted(ans))
