import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, C = minput()
box_info = [[] for _ in range(N)]
for _ in range(int(input_())):
    start, end, amount = minput()
    box_info[end - 1].append((start - 1, amount))

for i in range(N):
    box_info[i].sort(reverse=True)

ans = 0
carry = [0] * N
for end in range(N):
    for start, amount in box_info[end]:
        extra = min(amount, C - max(carry[start:end]))
        ans += extra
        for i in range(start, end):
            carry[i] += extra

print(ans)
