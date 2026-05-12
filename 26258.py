import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
points = [list(minput()) for _ in range(N)]
delta = []
for i in range(N - 1):
    d = points[i + 1][1] - points[i][1]
    if d > 0:
        delta.append(1)
    elif d < 0:
        delta.append(-1)
    else:
        delta.append(0)

Q = int(input_())
output = [''] * Q
queries = [[float(input_()), i] for i in range(Q)]
queries.sort()
pptr = 0
for qptr in range(Q):
    while pptr < N - 2 and points[pptr + 1][0] < queries[qptr][0]:
        pptr += 1
    output[queries[qptr][1]] = str(delta[pptr])
    qptr += 1

print('\n'.join(output))
