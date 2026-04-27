import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, l = minput()
aliases = [input_().rstrip() for _ in range(n)]
aliases.sort()

last = aliases[0]
ans = 0
last_a = 0

for i in range(1, n):
    cur = aliases[i]
    a = 0
    while a < l:
        if last[a] == cur[a]:
            a += 1
        else:
            break
    a += 1
    ans += max(last_a, a)
    last = cur
    last_a = a

print(ans + last_a)
