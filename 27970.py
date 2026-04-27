import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


s = input_().strip()
O = [i for i in range(len(s)) if s[i] == 'O']
print(sum(1 << i for i in O) % 1000000007)
