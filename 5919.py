import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
hay = [int(input_()) for _ in range(N)]
assert not sum(hay) % N
avg = sum(hay) // N
print(sum(abs(val - avg) for val in hay) >> 1)
