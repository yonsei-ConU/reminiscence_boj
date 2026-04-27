import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = set(minput())
mex = 0
while mex in A:mex += 1

if mex == 0: print(0)
elif sum(A) == 0: print(1)
else: print(mex + 2)
