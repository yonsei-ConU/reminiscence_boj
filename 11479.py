import sys
from algorithms import suffix_array, kasai
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


S = input_().rstrip()
sa = suffix_array(S)
lcp = kasai(S, sa)
N = len(S)
print((N * (N + 1) >> 1) - sum(lcp))
