import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


S = input_().rstrip()
p = k = 0
ans = 0

for s in S:
    if s == 'P':
        p += 1
        k -= 1
    else:
        k += 1
        p -= 1

    if p < 0 or k < 0:
        ans += 1
        p = max(p, 0)
        k = max(k, 0)

print(ans)
