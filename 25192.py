import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
ans = 0
greeted = set()
for _ in range(N):
    s = input_().rstrip()
    if s == "ENTER":
        greeted = set()
    elif s not in greeted:
        ans += 1
        greeted.add(s)

print(ans)
