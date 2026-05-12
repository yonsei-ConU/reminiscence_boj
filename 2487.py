# 1m 31.32s

import sys
from math import lcm
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def permutation_cycle_decomposition(l, permutation):
    processed = [False] * l
    cycles = []
    for i in range(l):
        if processed[i]:
            continue
        cycle = []
        pointer = i
        while not processed[pointer]:
            processed[pointer] = True
            cycle.append(pointer + 1)
            pointer = permutation[pointer] - 1
        if cycle:
            cycles.append(cycle)

    return cycles


N = int(input_())
A = list(minput())
p = permutation_cycle_decomposition(N, A)
p = list(map(len, p))
print(lcm(*p))
