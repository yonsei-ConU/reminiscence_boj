import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def H(s):
    return sum((ord(s[i]) - 96) * pm[len(s) - 1 - i] for i in range(len(s))) % MOD


MOD = 584039225158817291
B = 37

pm = [1]
for i in range(1499):
    pm.append(pm[-1] * B % MOD)

n = int(input_())
chorus = []

for _ in range(n):
    lyrics = input_().rstrip()

    # i글자, j+1번째 글자부터 시작 단 반복문 밖에서 j=-1
    for i in range(len(lyrics))[::-1]:
        d = defaultdict(list)
        h = H(lyrics[:i + 1])
        d[h].append((0, i + 1))
        for j in range(len(lyrics) - i - 1):
            a = ord(lyrics[j]) - 96
            c = ord(lyrics[i + j + 1]) - 96
            h = (h - a * pm[i]) % MOD
            h = (h * B + c) % MOD
            d[h].append((j + 1, i + j + 2))

        if (M := max(len(v) for v in d.values())) >= 2:
            max_cnt = M
            for key in d:
                if len(d[key]) == M:
                    start, end = d[key][0]
                    tmp = lyrics[start:end]
                    break
            break

    chorus.append(tmp)

for _ in range(int(input_())):
    lyrics = input_().rstrip()

    ans = []
    for i in range(n):
        if lyrics in chorus[i]:
            ans.append(str(i))

    print(' '.join(ans) if ans else -1)
