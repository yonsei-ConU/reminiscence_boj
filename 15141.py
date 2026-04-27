import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


h, w, n = minput()
ans = [[] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if n and not (i ^ j) & 1:
            ans[i].append('.')
            n -= 1
        else:
            ans[i].append('#')
if n:
    print("Impossible")
else:
    for row in ans:
        print(''.join(row))
