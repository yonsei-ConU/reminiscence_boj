import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
cards = []
for i in range(N):
    a, b = minput()
    if a > b: a, b = b, a
    cards.append((a, b - a))

cards.sort()
