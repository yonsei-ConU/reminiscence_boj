import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N1, N2, K = minput()
K -= 1
x = [N1, N2, abs(N1 - N2)]
for i in range(10):
    x.append(abs(x[-1] - x[-2]))
if K < len(x):
    exit(print(x[K]))
cur = len(x)
while not (x[-7] == x[-4] == x[-1]):
    x.append(abs(x[-1] - x[-2]))
    cur += 1
    if cur == K:
        exit(print(x[-1]))

x = x[-3:]
print(x)
next_term_count = x[-2] // x[-1]
print(next_term_count)
z = next_term_count + ((next_term_count - 1) >> 1)
for i in range(z + 2):
    x.append(abs(x[-1] - x[-2]))

print(x)
