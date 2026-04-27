import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
if N == 2:
    exit(print("*"))
n = N
factors = []
p = 2
while n != 1:
    while not n % p:
        factors.append(p)
        n //= p
    
