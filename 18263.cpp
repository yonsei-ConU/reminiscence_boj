#include <iostream>
#include <vector>
#include <algorithm>

template <typename T>
struct segment_tree {
    // ConU's non-recursive uniform segment tree implementation C++
    int n;
    std::vector<T> tree;
    T identity;

    T merge(T A, T B) {
        T ret;
        int a = 0, b = 0;
        while (a < A.size() && b < B.size()) {
            if (A[a] <= B[b]) {
                if (A[a] == B[b]) b++;
                ret.push_back(A[a++]);
            } else {
                ret.push_back(B[b++]);
            }
        }
        while (a < A.size()) {
            ret.push_back(A[a++]);
        }
        while (b < B.size()) {
            ret.push_back(B[b++]);
        }
        return ret;
    }

    segment_tree(const std::vector<T> &arr, T id) {
        n = 1;
        while (n < arr.size()) n <<= 1;
        identity = id;
        tree.assign(n << 1, identity);
        for (int i = 0; i < arr.size(); i++) {
            tree[n + i] = arr[i];
        }
        for (int i = n - 1; i > 0; i--) {
            tree[i] = merge(tree[2 * i], tree[2 * i + 1]);
        }
    }

    void update(int idx, T val) {
        idx += n;
        tree[idx] = val;
        while (idx > 1) {
            idx >>= 1;
            tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
        }
    }

    bool query(int l, int r, int val) {
        l += n;
        r += n;
        while (l <= r) {
            if (l & 1) {
                if (std::binary_search(tree[l].begin(), tree[l].end(), val)) return true;
                l++;
            }
            if (!(r & 1)) {
                if (std::binary_search(tree[r].begin(), tree[r].end(), val)) return true;
                r--;
            }
            l >>= 1;
            r >>= 1;
        }
        return false;
    }
};

struct HLD {
    std::vector<std::vector<int>> g;
    int root, N;
    int time = 0;
    std::vector<int> sz, depth, par, disc, esc, top;
    HLD(const std::vector<std::vector<int>> &input_tree, int r):
            root(r), N(input_tree.size()) {
        g.resize(N);
        sz.resize(N);
        depth.resize(N);
        par.resize(N);
        disc.resize(N);
        esc.resize(N);
        top.resize(N);
        get_g(input_tree, root, root);
        depth[root] = 0;
        decompose(root);
        hld_ett(root);
    }
    void get_g(const std::vector<std::vector<int>> &h, int cur, int parent) {
        for (int nxt : h[cur]) {
            if (nxt == parent) continue;
            g[cur].push_back(nxt);
            get_g(h, nxt, cur);
        }
    }
    void decompose(int cur) {
        sz[cur] = 1;
        for (int &nxt : g[cur]) {
            depth[nxt] = depth[cur] + 1;
            par[nxt] = cur;
            decompose(nxt);
            sz[cur] += sz[nxt];
            if (sz[nxt] > sz[g[cur][0]]) std::swap(nxt, g[cur][0]);
        }
    }
    void hld_ett(int cur) {
        disc[cur] = time++;
        for (int nxt : g[cur]) {
            top[nxt] = nxt == g[cur][0] ? top[cur] : nxt;
            hld_ett(nxt);
        }
        esc[cur] = time;
    }

    template <typename T>
    bool query(int l, int r, int val, segment_tree<T> &st) {
        while (top[l] ^ top[r]) {
            if (depth[top[l]] < depth[top[r]]) std::swap(l, r);
            if (st.query(disc[top[l]], disc[l], val)) return true;
            l = par[top[l]];
        }
        if (depth[l] > depth[r]) std::swap(l, r);
        // disc[l] for vertex, disc[l + 1] for edge
        return st.query(disc[l], disc[r], val);
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M;
    std::cin >> N >> M;
    std::vector<int> T(N);
    for (auto &i : T) std::cin >> i;
    std::vector<std::vector<int>> g(N);
    for (int i = 0; i < N - 1; i++) {
        int X, Y;
        std::cin >> X >> Y;
        g[--X].push_back(--Y);
        g[Y].push_back(X);
    }
    HLD hld(g, 0);
    std::vector<std::vector<int>> V(N);
    for (int i = 0; i < N; i++) {
        V[hld.disc[i]].push_back(T[i]);
    }
    auto st = segment_tree<std::vector<int>>(V, {});
    while (M--) {
        int A, B, C;
        std::cin >> A >> B >> C;
        bool ans = hld.query(A - 1, B - 1, C, st);
        if (ans) std::cout << 1;
        else std::cout << 0;
    }
    return 0;
}
