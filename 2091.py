import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


X, A, B, C, D = minput()

ans_amount = -1
ans_val = [0, 0, 0, 0]
for a in range(min(A, X) + 1):
    if (X - a) % 5: continue
    for b in range(min(B, (X - a) // 5) + 1):
        for c in range(min(C, (X - a - 5 * b) // 10) + 1):
            if (X - a - 10 * c - 5 * b) % 25:
                continue
            d = (X - a - 10 * c - 5 * b) // 25
            if d <= D and a + b + c + d > ans_amount:
                ans_amount = a + b + c + d
                ans_val = [a, b, c, d]

print(*ans_val)
