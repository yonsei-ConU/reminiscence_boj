import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())

ans_loc = 0
ans_val = 9999999999

A.sort()
ptr = 0
cur_val = sum(A)

for i in range(1, A[-1] + 1):
    cur_val = cur_val - (N - ptr) + ptr
    if cur_val < ans_val:
        ans_loc = i
        ans_val = cur_val
    while ptr < N and A[ptr] <= i:
        ptr += 1

print(ans_loc)
