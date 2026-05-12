import sys
from algorithms import knuth_morris_pratt
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


A = input_().rstrip() * 2
B = input_().rstrip()
ans = knuth_morris_pratt(A, B)
print(ans)
if 1 in ans:
    print(len(ans) - 1)
else:
    print(len(ans))
