import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
s = input_().strip()
depth = 150000
depth_last = [-1] * 300000
ans = 0
for i in range(n):
    paren = s[i]
    if paren == '(':
        depth += 1
        depth_last[depth] = i
    else:
        ans = max(ans, i + 1 - depth_last[depth])
        depth -= 1

print(ans)

