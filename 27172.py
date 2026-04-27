import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
x = list(minput())
x_appear = [False] * 1000001
for element in x: x_appear[element] = True
scores = {p: 0 for p in x}
for element in x:
    for bs in range(2 * element, 1000001, element):
        if x_appear[bs]:
            scores[element] += 1
            scores[bs] -= 1

print(*[scores[k] for k in x])
