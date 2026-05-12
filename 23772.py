import sys
from fractions import Fraction
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class segtree:
    def __init__(self, arr, func, identity):
        i = 1
        while i < len(arr): i <<= 1
        self.n = i
        self.tree = [identity] * (2 * self.n)
        self.func = func
        self.identity = identity
        for i in range(len(arr)):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, idx, val):
        idx += self.n
        self.tree[idx] = val
        while idx > 1:
            idx >>= 1
            self.tree[idx] = self.func(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, l, r):
        ret = self.identity
        l += self.n
        r += self.n
        while l <= r:
            if l % 2:
                ret = self.func(ret, self.tree[l])
                l += 1
            if not r % 2:
                ret = self.func(ret, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return ret


def ccw_sign(x1, y1, x2, y2, x3, y3):
    r = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
    if not r:
        return 0
    elif r > 0:
        return 1
    else:
        return -1


def dot_product(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2


def dist(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


xs, ys, xe, ye = minput()
n = int(input_())
visitors = [[], []]  # 0번째는 CCW = -1, 1번째는 CCW = 1
zero_ccw_count = [0, 0]  # 0번째는 (xs, ys)보다 작은거, 1번째는 큰거

# STEP 1: CCW를 이용해 점 분리하고, visitors 리스트에 각도를 넣음
for _ in range(n):
    x, y = minput()
    sgn = ccw_sign(x, y, xs, ys, xe, ye)
    # (xs, ys)보다 왼쪽인지 확인, 빨간 선분이 수직방향인 경우도 대비함
    if not sgn:
        if x < xs:
            idx = 0
        elif x > xs:
            idx = 1
        elif y < ys:
            idx = 0
        elif y > ys:
            idx = 1
        else:
            assert False
        zero_ccw_count[idx] += 1
    else:
        # a, b각은 무조건 0부터 ㅠ사이고, 이 범위에서 코사인은 감소함수이다
        # 정렬 편하게 하기 위해서, cos 대신 -cos 값을 집어넣음
        # a = (x, y), (xs, ys), (xe, ye) 사잇각
        # 내적제곱 / 거리제곱 구하고 부호만 따로 붙인다
        # 일단 그러기 위해서 각이 90도보다 큰지 작은지를 알아야 하고, 내적 부호 씀...
        dot1 = dot_product(x - xs, y - ys, xe - xs, ye - ys)
        cos_a = Fraction(dot1 ** 2, dist(x, y, xs, ys))
        if dot1 > 0: cos_a *= -1
        # b = (x, y), (xe, ye), (xs, ys) 사잇각
        dot2 = dot_product(x - xe, y - ye, xs - xe, ys - ye)
        cos_b = Fraction(dot2 ** 2, dist(x, y, xe, ye))
        if dot2 > 0: cos_b *= -1
        if sgn == 1:
            visitors[1].append((cos_a, cos_b))
        else:
            visitors[0].append((cos_a, cos_b))

# STEP 2: CCW가 0인 값들 먼저 계산
ans = 0
for x in zero_ccw_count:
    ans += x * (x - 1) // 2

# STEP 3: a, b각 정렬
visitors[0].sort()
visitors[1].sort()

# STEP 4: 'segtree'
for z in range(2):
    v = visitors[z]
    # b각을 좌표압축해야 된다
    b = [asdf[1] for asdf in v]
    b_distinct = sorted(set(b))
    b_rank = {b_distinct[i]: i for i in range(len(b_distinct))}

    st = segtree([0] * len(v), lambda p, q: p + q, 0)
    for i in range(len(v)):
        # right = b각의 좌표압축된 값
        right = b_rank[v[i][1]]
        ans += st.query(0, right)
        st.update(right, st.query(right, right) + 1)

# 하 드디어 다짰다
print(ans)
