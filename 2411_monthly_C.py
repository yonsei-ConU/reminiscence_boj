import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


X, Q = minput()
lst = [X]
for i in range(1, 100001):
    X -= X % i
    X += i
    lst.append(X)

diff = lst[-1] - lst[-2]

for _ in range(Q):
    Ai = int(input_())
    if Ai <= 100000:
        print(lst[Ai])
    else:
        print(lst[100000] + diff * (Ai - 100000))
