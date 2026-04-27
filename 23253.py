import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
for _ in range(M):
    k = int(input_())
    l = list(minput())
    if l != sorted(l, reverse=True):
        print('No')
        exit()
print('Yes')
