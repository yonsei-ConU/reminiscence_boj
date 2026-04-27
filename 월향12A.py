import sys
input_ = sys.stdin.readline
def minput(): return map(int, input().split())

N, M = minput()
ans = 0

for _ in range(N):
    s = input_()
    ans += s.count('O') > s.count('X')

print(ans)
