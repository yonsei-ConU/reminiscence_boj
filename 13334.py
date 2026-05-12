import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
segment = [list(minput()) for _ in range(n)]
d = int(input_())
raw = []
s = set()

for a, b in segment:
    if a > b: a, b = b, a
    a, b = b, a + d
    if a <= b:
        raw.append((a, -1))
        raw.append((b, 1))
        s.add(a)
        s.add(b)

raw.sort()
ans = 0
cur_sum = 0

for _, delta in raw:
    cur_sum -= delta
    ans = max(ans, cur_sum)

print(ans)
