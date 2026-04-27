import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
if -32768 <= N <= 32767:
    print('short')
elif -2147483648 <= N <= 2147483647:
    print('int')
else:
    print('long long')
