import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


ans = 0
for _ in range(int(input_())):
    ans += sum(list(minput()))

print(ans)
