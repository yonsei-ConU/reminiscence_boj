import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
A_raw = list(minput())
A = []
for element in A_raw:
    binary = element.bit_count()
    ternary = 0
    e = element
    while e:
        ternary += e % 3 == 1
        e //= 3
    A.append((binary, ternary))

print(A)
