import sys
from heapq import heapify, heappop
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


p, v = minput()
pedestal = [sorted(list(minput())) for _ in range(p)]

pedestal_numbers = defaultdict(list)
for i in range(p): pedestal_numbers[tuple(pedestal[i])].append(i + 1)
heapify(pedestal)

vase = list(minput())
vase_numbers = defaultdict(list)
for i in range(v):
    vase_numbers[vase[i]].append(i)
vase.sort()

ptr = 0
ans = [0] * v

while ptr < v:
    vi = vase[ptr]
    while pedestal:
        a, b = heappop(pedestal)
        if a > vi:
            exit(print('impossible'))
        elif a != vi != b:
            continue
        else:
            ans[vase_numbers[vi].pop()] = pedestal_numbers[(a, b)].pop()
            break
    else:
        exit(print('impossible'))
    ptr += 1

for a in ans: print(a)

'''
4 3
1 2
3 4
5 6
7 8
1 3 8
'''
