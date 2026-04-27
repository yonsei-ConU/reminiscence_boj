import sys
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
            cycle.append(pointer)
            pointer = permutation[pointer]
        if cycle:
            cycles.append(cycle)

    return cycles


N, K, M = minput()
swaps = []
for i in range(min(M, K)):
    a, b = minput()
    swaps.append((a - 1, b - 1))

positions = list(range(N))
reachable = [{i} for i in range(N)]

for a, b in swaps:
    positions[a], positions[b] = positions[b], positions[a]
    reachable[positions[a]].add(a)
    reachable[positions[b]].add(b)

if M <= K: exit(print(*[len(a) for a in reachable], sep='\n'))

cycles = permutation_cycle_decomposition(N, positions)

