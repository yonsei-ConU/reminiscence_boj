import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


a1, a0 = minput()
c = int(input_())
n0 = int(input_())
fn0 = a1 * n0 + a0
cgn0 = c * n0
if fn0 <= cgn0 and a1 <= c:
    print(1)
else:
    print(0)
