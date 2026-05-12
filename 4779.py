import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


ans = ['-']
for i in range(12):
    ans.append(ans[-1] + ' ' * (3 ** i) + ans[-1])

for line in sys.stdin:
    print(ans[int(line)])
