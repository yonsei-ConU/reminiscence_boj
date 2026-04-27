import sys
input_ = sys.stdin.readline
def minput(): return map(lambda x: int(x) - 1, input_().split())


for _ in range(int(input_())):
    n = int(input_())
    selected = list(minput())
    idx = 0
    cycle_info = [-1] * n
    ans = 0
    for i in range(n):
        if cycle_info[i] != -1:
            continue
        cnt = 1
        visited = {i: 0}
        cur = i
        while True:
            cycle_info[cur] = idx
            nxt = selected[cur]
            if cycle_info[nxt] == -1:
                pass
            elif cycle_info[nxt] == idx:
                flag = visited[nxt]
                break
            else:
                flag = -1
                break
            visited[nxt] = cnt
            cnt += 1
            cur = nxt
        if flag > -1:
            ans += flag
        else:
            ans += cnt
        idx += 1
    print(ans)
