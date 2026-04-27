import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
p, q, r, s = minput()
A = [0] * (n + 1)
A[1] = int(input_())

for i in range(2, n + 1):
    if i % 2:
        A[i] = A[i // 2] * r + s
    else:
        A[i] = A[i // 2] * p + q

print(sum(A))    
