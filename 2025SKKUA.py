import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
if N & 1:
    print("Bob")
else:
    print("Alice")
