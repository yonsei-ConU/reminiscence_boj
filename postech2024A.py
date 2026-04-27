import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())

l = False
k = False
p = False

for i in range(3):
    s = input()[0]
    if s == 'l':
        l = True
    elif s == 'k':
        k = True
    elif s == 'p':
        p = True

print('GPLOONBIAXL'[not(l and k and p)::2])
