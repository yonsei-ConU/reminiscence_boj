import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
g = [[] for _ in range(N)]
indegree = [0] * N

for i in range(N):
    X, Y = minput()
    X -= 1; Y -= 1
    g[i] = [X, Y]
    indegree[X] += 1; indegree[Y] += 1
print(indegree)
res = []
for i in range(N):
    X, Y = g[i]
    if indegree[i] < indegree[X] and indegree[i] < indegree[Y]:
        res.append('N')
    else:
        res.append('Y')

print(''.join(res))
