import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
triangles = set()

for _ in range(N):
    t = list(minput())
    for length in t:
        if length in triangles:
            exit(print(1))
    for length in t:
        triangles.add(length)

print(0)
