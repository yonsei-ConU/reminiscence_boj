import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


num = input_().rstrip().replace('-', '')
print(len(set(list(num))))
