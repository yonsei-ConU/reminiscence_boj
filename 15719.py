import sys
from collections import Counter
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = Counter(tuple(minput()))
print(A.most_common(1)[0][0])
