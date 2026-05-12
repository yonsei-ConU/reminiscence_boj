import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, m = minput()
original = [list(minput()) for _ in range(m)]
ans_val = 101
ans_indices = []

for i in range(n - 1):
    poll = {}
    p = q = 0

    for idx in range(m):
        other = original[idx][i]
        opponent = original[idx][-1]
        poll[(other - opponent, other, opponent, idx)] = idx + 1
        p += other
        q += opponent
    if p >= q:
        ans_val = 0
        ans_indices = []
        break

    temp_ans = 0
    temp_trace = []
    for key in sorted(poll.keys()):
        idx = poll[key]
        temp_ans += 1
        temp_trace.append(idx)
        p -= key[1]
        q -= key[2]
        if p >= q:
            break

    if temp_ans < ans_val:
        ans_val = temp_ans
        ans_indices = temp_trace[:]

print(ans_val)
if ans_indices: print(*ans_indices)