import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


v, i = divmod(int(input_()), 5)
print("V" * v + "I" * i)
