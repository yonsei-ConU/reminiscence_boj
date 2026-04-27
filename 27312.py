import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


M, N, Q = minput()
a = list(minput())
ans = []
for i in range(1, M + 1):
    print(f"? {i} {i}", flush=True)
    result = int(input_())
    if result == 1:
        ans.append('2')
    else:
        ans.append('1')

while len(ans) < N:
    ans.append('1')

print(f"! {' '.join(ans)}")
