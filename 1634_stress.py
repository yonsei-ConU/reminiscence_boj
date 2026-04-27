import sys
from itertools import combinations
from random import shuffle
input_ = sys.stdin.readline
def minput(): return map(lambda x: int(x) - 1, input_().split())


def is_clique(graph, vertices):
    for u in vertices:
        for v in vertices:
            if u != v and v not in graph[u]:
                return False
    return True


def find_maximum_clique(graph):
    n = len(graph)
    max_clique = []

    for r in range(1, n + 1):
        for subset in combinations(tuple(range(n)), r):
            if is_clique(graph, subset) and len(subset) > len(max_clique):
                max_clique = subset

    return max_clique


def naive():
    g = [[] for _ in range(len(T1))]
    for i in range(len(T1)):
        for j in range(i + 1, len(T1)):
            c = (i ^ j).bit_length()
            x = T2_rev[i]
            y = T2_rev[j]
            if c == (x ^ y).bit_length():
                g[T2[i]].append(T2[j])
                g[T2[j]].append(T2[i])
    return len(find_maximum_clique(g))


def solve():
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
    return max_size


tc = 0
while True:
    try:
        k = 3
        T1 = list(range(8))
        T1_rev = [0] * len(T1)
        for i in range(len(T1)): T1_rev[T1[i]] = i
        T2 = list(range(8))
        shuffle(T2)
        T2 = [T1_rev[i] for i in T2]
        T1 = list(range(len(T2)))
        T2_rev = [0] * len(T2)
        for i in range(len(T2)): T2_rev[T2[i]] = i

        x = naive()
        y = solve()
        if x == y:
            tc += 1
        else:
            print('found')
            print(T2)
            break
    except KeyboardInterrupt:
        print(f"{tc} testcases passed")
        break
