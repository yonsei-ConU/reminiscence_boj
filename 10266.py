import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
first = list(minput())
first = [first[i + 1] - first[i] for i in range(n - 1)] + 
second = list(minput())
first = [second[i + 1] - second[i] for i in range(n - 1)]
