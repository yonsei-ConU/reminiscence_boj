import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    N = int(input_())
    if N % 3 == 2 or not N % 9:
        print('TAK')
    else:
        print('NIE')
