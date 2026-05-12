import sys
input_ = sys.stdin.readline
def minput(): return map(lambda x: int(x) + 1, input_().split())


l = int(input_())
w = list(minput())
if w.count(1) == l:
    exit(print(0))
else:
    ans = 1
    for v in w:
        ans = (ans * v) % 9
    ans = (ans - 1) % 9
    if not ans:
        print(9)
    else:
        print(ans)
