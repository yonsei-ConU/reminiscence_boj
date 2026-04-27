import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class Node:
    def __init__(self, depth, parent):
        global node_cnt
        self.idx = node_cnt
        node_cnt += 1
        self.depth = depth
        self.parent = parent


N = int(input_())
node_cnt = 0
tree = [dict() for _ in range(15)]
for _ in range(N):
    pass
