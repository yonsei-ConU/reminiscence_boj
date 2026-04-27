import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def dfs(path, start, sum_left, cnt_left):
    if not cnt_left:
        if not sum_left:
            print('(' + ','.join(path) + ')')
        return
    for cur in range(start, m + 1):
        if cur > sum_left:
            break
        path.append(str(cur))
        dfs(path, cur, sum_left - cur, cnt_left - 1)
        path.pop()


for tc in range(1, int(input_()) + 1):
    n, m, s = minput()
    print(f"Case {tc}:")
    dfs([], 1, s, n)
