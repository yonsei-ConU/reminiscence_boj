import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A = [[1, 2, 4, 3], [1, 3, 2, 4]][N & 1]
ans = [str(A[i & 3] + (i >> 2 << 2)) for i in range(N)]
print("YES")
print(' '.join(ans))
