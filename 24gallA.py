import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
s = input_().strip()
while 'PS4' in s or 'PS5' in s:
    s = s.replace('PS4', 'PS').replace('PS5', 'PS')

print(s)
