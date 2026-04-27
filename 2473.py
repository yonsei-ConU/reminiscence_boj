import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
l = sorted(list(minput()))
ans_val = 2**33
ans_idx = [0, 0, 0]
for i in range(N):
    start = 0
    end = N - 1

    while start < end:
        if start == i: start += 1
        if end == i: end -= 1
        if not (0 <= start < end < N): break

        tmp = l[start] + l[end] + l[i]
        if abs(tmp) < ans_val:
            ans_idx = [start, end, i]
            ans_val = abs(tmp)
        if tmp > 0:
            end -= 1
        else:
            start += 1

a, b, c = sorted(ans_idx)
print(l[a], l[b], l[c])
