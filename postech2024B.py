import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

N = int(input_())
ans = 0
for _ in range(N):
    l = list(minput())
    for i in range(3):
        if l[i] == -1:
            l[i] = 10000000
    ans += +(l == sorted(l) and l[0] != 10000000)

print(ans)
