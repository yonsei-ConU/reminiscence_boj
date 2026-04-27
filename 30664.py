import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


while True:
    x = int(input_())
    if not x:
        break
    if not x % 42:
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")
