import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


A, B = minput()
MOD = 10 ** 9 + 7
print((pow(A, B, MOD) - 1) * pow(A - 1, -1, MOD) % MOD if A != 1 else B % MOD)
