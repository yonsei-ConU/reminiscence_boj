import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
intervals = sorted([list(minput()) for _ in range(n)])
ans = []
start, end = intervals[0]
for s, e in intervals[1:]:
    if s <= end:
        end = max(end, e)
    else:
        ans.append([start, end])
        start = s
        end = e

ans.append([start, end])

for s, e in ans:
    print(s, e)
