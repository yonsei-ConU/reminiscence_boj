import sys
input_ = sys.stdin.readline
def minput(): return map(lambda x: int(x) - 1, input_().split())


k = int(input_())
T1 = list(minput())
T1_rev = [0] * len(T1)
for i in range(len(T1)): T1_rev[T1[i]] = i
T2 = list(minput())
T2 = [T1_rev[i] for i in T2]
T2_rev = [0] * len(T2)
for i in range(len(T2)): T2_rev[T2[i]] = i

max_size = 0
for i in range(len(T1)):
    current_size = 1
    for j in range(i + 1, len(T1)):
        c = (i ^ j).bit_length()
        x = T2_rev[i]
        y = T2_rev[j]
        if c == (x ^ y).bit_length():
            current_size += 1
    max_size = max(max_size, current_size)

print(max_size)
