import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for tc in range(1, int(input_()) + 1):
    grid = [list(minput()) for _ in range(6)]
    chk = True
    for i in range(6):
        if len(set(grid[i])) != 6:
            chk = False
            break
    for j in range(6):
        if len(set([grid[i][j] for i in range(6)])) != 6 or len(set([grid[i][i] for i in range(6)])) != 6:
            chk = False
            break
    print(f"Case#{tc}: {+chk}")
