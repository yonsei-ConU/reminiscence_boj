import sys
from itertools import permutations
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


rectangles = [list(minput()) for _ in range(4)]
for p in permutations(rectangles):
    for mask in range(16):
        w = []
        h = []
        for i in range(4):
            if mask & (1 << i):
                w.append(p[i][1])
                h.append(p[i][0])
            else:
                w.append(p[i][0])
                h.append(p[i][1])
        if w[0] == w[1] + w[2] + w[3] and h[1] == h[2] == h[3] and h[0] + h[1] == w[0]:
            exit(print(1))
        elif w[0] == w[1] and w[0] == w[2] + w[3] and h[2] == h[3] and h[0] + h[1] + h[2] == w[0]:
            exit(print(1))
        elif w[0] == w[1] == w[2] == w[3] and h[0] + h[1] + h[2] + h[3] == w[0]:
            exit(print(1))
        elif w[0] == w[2] and w[1] == w[3] and h[0] + h[2] == h[1] + h[3]:
            exit(print(1))
        elif w[0] + w[1] == w[2] + w[3] and h[0] == h[1] and h[2] == h[3] and w[0] + w[1] == h[0] + h[2]:
            exit(print(1))
        elif w[0] + w[1] == w[3] and h[0] == h[1] and h[0] + h[3] == h[2] and h[2] == w[3] + w[2]:
            exit(print(1))

print(0)
