import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


print(['Duck', 'Goose'][int(input_()) & 1])
