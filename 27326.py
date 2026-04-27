import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = list(minput())
for i in range(1, N + 1):
    if A.count(i) == 1:
        print(i)
