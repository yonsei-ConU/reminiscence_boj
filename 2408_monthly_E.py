import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    s = set(map(lambda x: int(x) % 3, input_().split()))
    print("YNEOS"[len(s) == 2::2])
