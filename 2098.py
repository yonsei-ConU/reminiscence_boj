import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
costs = [list(minput()) for _ in range(N)]
dp = [[20000000] * (1 << N) for _ in range(N)]
prev = [[20000000] * (1 << N) for _ in range(N)]

for i in range(N):
    t = 20000000
    for j in range(N):
        if costs[i][j]:
            t = min(t, costs[i][j])
    prev[i][1 << i] = t

for cnt in range(1, N):
    for cur_city in range(N):
        for mask in range(1 << N):
            
