#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

template <typename T>
struct SegNode {
    SegNode *l, *r;
    T val;
    SegNode() : l(nullptr), r(nullptr) {}
    explicit SegNode(T x) : l(nullptr), r(nullptr), val(x) {}
    SegNode(SegNode *left, SegNode *right, T x) : l(left), r(right), val(x) {}
};

template <typename T>
class PersistentSeg {
public:
    PersistentSeg(std::vector<T> arr, T id) : n(arr.size()), identity(id) {
        roots.clear();
        roots.push_back(new SegNode<T>);
        build(0, n - 1, roots[0], arr);
    }

    void update(int idx, T val) {
        SegNode<T> *new_root = DoUpdate(0, n - 1, roots.back(), idx, val);
        roots.push_back(new_root);
    }

    T query(int l, int r, int time) {
        return DoQuery(l, r, 0, n - 1, roots[time]);
    }

private:
    int n;
    T identity;
    std::vector<SegNode<T>*> roots;

    T merge(T a, T b) {
        return a + b;
    }

    void build(int l, int r, SegNode<T> *cur, const std::vector<T> &arr) {
        if (l == r) {
            cur->val = arr[l];
        } else {
            int mid = l + ((r - l) >> 1);
            cur->l = new SegNode<T>;
            build(l, mid, cur->l, arr);
            cur->r = new SegNode<T>;
            build(mid + 1, r, cur->r, arr);
            cur->val = merge(cur->l->val, cur->r->val);
        }
    }

    SegNode<T> *DoUpdate(int l, int r, SegNode<T> *cur, int idx, T val) {
        if (l == r) return new SegNode<T>(val);
        int mid = l + ((r - l) >> 1);
        if (idx <= mid) {
            auto ret = new SegNode<T>(DoUpdate(l, mid, cur->l, idx, val), cur->r, val);
            ret->val = merge(ret->l->val, ret->r->val);
            return ret;
        } else {
            auto ret = new SegNode<T>(cur->l, DoUpdate(mid + 1, r, cur->r, idx, val), val);
            ret->val = merge(ret->l->val, ret->r->val);
            return ret;
        }
    }

    T DoQuery(int ql, int qr, int l, int r, SegNode<T> *cur) {
        if (qr < l || r < ql) return identity;
        else if (ql <= l && r <= qr) return cur->val;
        else {
            int mid = l + ((r - l) >> 1);
            return merge(DoQuery(ql, qr, l, mid, cur->l), DoQuery(ql, qr, mid + 1, r, cur->r));
        }
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int T;
    std::cin >> T;
    while (T--) {
        int n, m;
        std::cin >> n >> m;
        std::pair<int, int> pos[n];
        for (auto &i : pos) std::cin >> i.first >> i.second;
        std::sort(pos, pos + n);
        PersistentSeg<int> pst(std::vector<int>(100001, 0), 0);
        int time = 0;
        std::vector<int> times;
        int lastX = -1;
        for (auto &[x, y] : pos) {
            while (lastX < x) {
                times.push_back(time);
                lastX++;
            }
            pst.update(y, pst.query(y, y, time) + 1);
            time++;
        }
        while (lastX <= 100000) {
            times.push_back(time);
            lastX++;
        }
        ll ans = 0;
        while (m--) {
            int l, r, b, t;
            std::cin >> l >> r >> b >> t;
            ans += pst.query(b, t, times[r + 1]) - pst.query(b, t, times[l]);
        }
        std::cout << ans << '\n';
    }
    return 0;
}
