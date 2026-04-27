import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def make_sample(lst):
    pivot = min(lst)
    return [value - pivot for value in sorted(lst)]


N = int(input_())
song = [int(input_()) for _ in range(N)]
C = int(input_())
rsc = make_sample([int(input_()) for _ in range(C)])

ans = []
for start in range(N - C + 1):
    if rsc == make_sample(song[start:start + C]):
        ans.append(start + 1)

print(len(ans))
for a in ans: print(a)
