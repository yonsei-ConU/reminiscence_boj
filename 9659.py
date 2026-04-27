import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


print("CSYK"[int(input_()) & 1::2])
