import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
D = [int(input_()) for _ in range(N)]

money = 0
debt = 0
leftmost_debt_idx = -1
ans = N

for i in range(N):
    x = D[i]
    if x > 0:
        money += x
        if money >= debt and leftmost_debt_idx != -1:
            ans += 2 * (i - leftmost_debt_idx)
            money -= debt
            debt = 0
            leftmost_debt_idx = -1
    else:
        x = -x
        if money >= x:
            money -= x
        else:
            if leftmost_debt_idx == -1:
                leftmost_debt_idx = i
            debt += x

print(ans)
