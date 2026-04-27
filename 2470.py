import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
l = sorted(list(minput()))
start = 0
end = N - 1
ans_val = 2**31
ans_idx = [0, 0]

while start < end:
    tmp = l[start] + l[end]
    if abs(tmp) < ans_val:
        ans_idx = [start, end]
        ans_val = abs(tmp)
    if tmp > 0:
        end -= 1
    else:
        start += 1

m, M = ans_idx
print(l[m], l[M])
