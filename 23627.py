import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


print('not ' * (1 - input_().rstrip().endswith('driip')) + 'cute')
