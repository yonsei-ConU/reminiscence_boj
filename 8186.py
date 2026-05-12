import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def substring_hash(l, r):
    ret = [0, 0]
    for j in range(2):
        ret[j] = (prefix_hash[r][j] - prefix_hash[l - 1][j] * pow(B, r - l + 1, MOD[j])) % MOD[j]
    return tuple(ret)


def substring_hash_rev(l, r):
    ret = [0, 0]
    l, r = n - 1 - r, n - 1 - l
    for j in range(2):
        ret[j] = (prefix_hash_reverse[r][j] - prefix_hash_reverse[l - 1][j] * pow(B, r - l + 1, MOD[j])) % MOD[j]
    return tuple(ret)


n = int(input_())
a = list(minput())
a_rev = a[::-1]
MOD = [998244353, 2147483647]
B = 200003
prefix_hash = [[a[0], a[0]]]
# 여기에는 오른쪽에서부터 i번째까지의 해시값이 들어있다 (n - i - 1 부터 n - 1 까지)
prefix_hash_reverse = [[a_rev[0], a_rev[0]]]
for i in range(1, n):
    prefix_hash.append([0, 0])
    prefix_hash_reverse.append([0, 0])
    for j in range(2):
        prefix_hash[i][j] = (prefix_hash[i - 1][j] * B + a[i]) % MOD[j]
        prefix_hash_reverse[i][j] = (prefix_hash_reverse[i - 1][j] * B + a_rev[i]) % MOD[j]

prefix_hash.append([0, 0])
prefix_hash_reverse.append([0, 0])

ans_val = 0
ans_k = []
for k in range(1, n + 1):
    s = set()
    t = 0
    ptr = 0
    while ptr + k <= n:
        h1 = substring_hash(ptr, ptr + k - 1)
        if h1 not in s:
            t += 1
        h2 = substring_hash_rev(ptr, ptr + k - 1)
        s.add(h1)
        s.add(h2)
        ptr += k
    if t > ans_val:
        ans_val = t
        ans_k = [k]
    elif t == ans_val:
        ans_k.append(k)

print(ans_val, len(ans_k))
print(*ans_k)
