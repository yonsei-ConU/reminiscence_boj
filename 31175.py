import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, a, b = minput()
a -= 1
b -= 1
a, b = b, a
if a < n//2 and b < n//2:
    ans1 = 'UL' * (n - 1)
    ans2 = 'R' * a + 'D' * b
elif a < n//2 and b >= n//2:
    ans1 = 'DL' * (n - 1)
    ans2 = 'R' * a + 'U' * (n - 1 - b)
elif a >= n//2 and b < n//2:
    ans1 = 'UR' * (n - 1)
    ans2 = 'L' * (n - 1 - a) + 'D' * b
else:
    ans1 = 'DR' * (n - 1)
    ans2 = 'L' * (n - 1 - a) + 'U' * (n - 1 - b)

print(ans1 + ans2)
