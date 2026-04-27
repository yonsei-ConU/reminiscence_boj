#include <iostream>
#include <vector>

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
struct PersistentSeg {
    PersistentSeg(std::vector<T> arr, T id) : n(arr.size()), identity(id) {
        roots.clear();
        roots.push_back(new SegNode<T>);
        build(0, n - 1, roots[0], arr);
    }

    void update(int idx, T val, int time = -1) {
        SegNode<T> *root;
        if (time == -1) root = roots.back();
        else root = roots[time];
        SegNode<T> *new_root = DoUpdate(0, n - 1, root, idx, val);
        roots.push_back(new_root);
    }

    T query(int l, int r, int time = -1) {
        SegNode<T> *root;
        if (time == -1) root = roots.back();
        else root = roots[time];
        return DoQuery(l, r, 0, n - 1, root);
    }

    inline int getTime() {
        return (int)roots.size() - 1;
    }

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

    int M;
    std::cin >> M;
    int top = 0;
    int times[500001] = {0};
    PersistentSeg<int> pst(std::vector<int>(524288, 0), 0);
    while (M--) {
        int q;
        std::cin >> q;
        if (q == 1) {
            int x;
            std::cin >> x;
            pst.update(x, pst.query(x, x) + 1);
            times[++top] = pst.getTime();
        } else if (q == 2) {
            int L, R, x;
            std::cin >> L >> R >> x;
            int y = 0;
            int d = 262144;
            SegNode<int> *curR = pst.roots[times[R]];
            SegNode<int> *curL = pst.roots[times[L - 1]];
            while (d) {
                bool nxt;
                if (x & d) nxt = (curR->l->val == curL->l->val);
                else nxt = (curR->r->val > curL->r->val);
                if (nxt) {
                    y += d;
                    curL = curL->r;
                    curR = curR->r;
                } else {
                    curL = curL->l;
                    curR = curR->l;
                }
                d >>= 1;
            }
            std::cout << y << '\n';
        } else if (q == 3) {
            int k;
            std::cin >> k;
            top -= k;
            pst.update(0, pst.query(0, 0, times[top]), times[top]);
            times[top] = pst.getTime();
        } else if (q == 4) {
            int L, R, x;
            std::cin >> L >> R >> x;
            std::cout << pst.query(0, x, times[R]) - pst.query(0, x, times[L - 1]) << '\n';
        } else {
            int L, R, k;
            std::cin >> L >> R >> k;
            SegNode<int> *curR = pst.roots[times[R]];
            SegNode<int> *curL = pst.roots[times[L - 1]];
            int l = 0;
            int r = 524287;
            while (l < r) {
                int det = curR->l->val - curL->l->val;
                if (det < k) {
                    curR = curR->r;
                    curL = curL->r;
                    l = ((l + r) >> 1) + 1;
                    k -= det;
                } else {
                    curR = curR->l;
                    curL = curL->l;
                    r = (l + r) >> 1;
                }
            }
            std::cout << l << '\n';
        }
    }
    return 0;
}
