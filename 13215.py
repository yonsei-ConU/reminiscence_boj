import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class MergeSortTree:
    def __init__(self, arr):
        i = 1
        while i < len(arr): i <<= 1
        self.n = i
        self.tree = [[] for _ in range(2 * self.n)]
        for i in range(len(arr)):
            self.tree[self.n + i] = [arr[i]]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.merge(self.tree[2 * i], self.tree[2 * i + 1])

    def merge(self, left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def query(self, l, r, k):
        l += self.n
        r += self.n
        result = 0
        while l <= r:
            if l % 2:
                result += self.count_less_equal(self.tree[l], k)
                l += 1
            if not r % 2:
                result += self.count_less_equal(self.tree[r], k)
                r -= 1
            l >>= 1
            r >>= 1
        return result

    def count_less_equal(self, arr, k):
        lo, hi = -1, len(arr)
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if arr[mid] <= k:
                lo = mid
            else:
                hi = mid
        return hi


N, K = minput()
satisfaction = list(minput())
ps = [0]
cur_sum = 0
for i in range(N):
    cur_sum += satisfaction[i]
    ps.append(cur_sum)

mst = MergeSortTree(ps)
ans = 0
for k in range(1, N + 1):
    threshold = ps[k] - K
    ans += mst.query(0, k - 1, threshold)

print(ans)
