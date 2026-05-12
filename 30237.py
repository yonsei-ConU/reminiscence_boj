import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    n = int(input_())
    counts = []
    total_counts = [0] * 50
    for __ in range(n):
        k, *s = minput()
        tmp = [0] * 50
        for element in s:
            tmp[element - 1] += 1
            total_counts[element - 1] += 1
        counts.append(tmp[:])
    tot = sum(bool(x) for x in total_counts)
    ans = 0
    for i in range(50):
        cur_counts = [0] * 50
        for cnt in counts:
            if not cnt[i]:
                for j in range(50):
                    cur_counts[j] += cnt[j]
        t = sum(bool(x) for x in cur_counts)
        if t != tot:
            ans = max(ans, t)

    print(ans)
