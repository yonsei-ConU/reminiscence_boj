import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
ans = []
cur = 0
visited = [False] * N
visited[0] = True
cnt = 1

while cnt < N:
    print("maze", flush=True)
    k = int(input_()) - 1
    if not visited[k]:
        visited[k] = True
        cnt += 1
        ans.append((cur + 1, k + 1))
    cur = k

print("answer")
for u, v in ans:
    print(u, v)

sys.stdout.flush()
