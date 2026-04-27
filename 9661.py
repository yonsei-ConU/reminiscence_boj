import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
if N % 5 in [0, 2]:
    print("CY")
else:
    print("SK")
