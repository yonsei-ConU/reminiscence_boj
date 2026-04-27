import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


while True:
    n, k = minput()
    if not n: break
    if n == 1:
        input_()
        print(0)
        continue
    tree = list(minput())
    last = tree[0]
    streak = 1
    depth = 0
    depth_lst = [last]
    for i in range(1, N):
        if tree[i] - last == 1:
            streak += 1
        else:
