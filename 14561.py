import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    A, n = minput()
    lst = []
    while A:
        lst.append(A % n)
        A //= n
    print(+(lst == lst[::-1]))
