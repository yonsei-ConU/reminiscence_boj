import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


K = int(input_())
x = K.bit_length()
for i in range(x):
    if K == (1 << i):
        exit(print(K, 0))
for i in range(x):
    if K & (1 << i):
        t = x - i
        break
else:
    assert False

print(1 << x, t)
