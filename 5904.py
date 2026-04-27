import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_()) - 1
lengths = [3]
while lengths[-1] <= N: lengths.append(2 * lengths[-1] + len(lengths) + 3)
start = 0
end = lengths[-1]
for i in range(len(lengths) - 1)[::-1]:
    if N < start + lengths[i]:
        end = start + lengths[i]
    elif N < end - lengths[i]:
        if N == start + lengths[i]:
            exit(print('m'))
        else:
            exit(print('o'))
    else:
        start = end - lengths[i]

print('om'[start == N])
