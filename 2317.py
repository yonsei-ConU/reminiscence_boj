import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, K = minput()
lion = [int(input_()) for _ in range(K)]
human = [int(input_()) for _ in range(N - K)]
if len(lion) == 1:
    lst = human + lion
    exit(print(max(lst) - min(lst)))

M, m = max(human), min(human)
if max(lion) >= M:
    
