import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    h, w = minput()
    building = []
    for i in range(h):
        building.append(input_().rstrip())
