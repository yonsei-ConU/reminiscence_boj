import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())
print(min(A.count(0), A.count(1)))
