#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

ll ans = 0;

template <typename T>
struct segment_tree {
    // ConU's non-recursive uniform segment tree implementation C++
    int n;
    std::vector<T> tree;
    T identity;

    T merge(T a, T b) {
        return std::max(a, b);
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

    T query(int l, int r) {
        l += n;
        r += n;
        T ret_left = identity;
        T ret_right = identity;
        while (l <= r) {
            if (l & 1) {
                ret_left = merge(ret_left, tree[l++]);
            }
            if (!(r & 1)) {
                ret_right = merge(tree[r--], ret_right);
            }
            l >>= 1;
            r >>= 1;
        }
        return merge(ret_left, ret_right);
    }
};

void dfs(int l, int r, ll score, segment_tree<ll> &st, const std::vector<ll> &h) {
    if (r - l == 1) {
        ans = std::max(ans, score + std::min(h[l], h[r]));
        return;
    } else {
        ll cur = std::min(h[l], h[r]);
        ll mx = st.query(l + 1, r - 1);
        int last = l;
        ll dscore = (r - l) * (cur - mx);
        for (int nxt = l + 1; nxt < r; nxt++) {
            if (h[nxt] == mx) {
                dfs(last, nxt, score + dscore, st, h);
                last = nxt;
            }
        }
        if (last != l) {
            dfs(last, r, score + dscore, st, h);
        }
    }
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int T;
    std::cin >> T;
    while (T--) {
        ans = 0;
        int N;
        std::cin >> N;
        std::vector<ll> h(N);
        for (auto &i : h) std::cin >> i;
        segment_tree<ll> st(h, 0);
        ll mx = st.query(0, N - 1);
        if (mx == 0 || N == 1) {
            std::cout << "0\n";
            continue;
        }
        // index 0 -> max first
        int left = 0;
        ll cur_max = h[0];
        for (int idx = 1; idx < N; idx++) {
            if (h[idx] >= cur_max) {
                dfs(left, idx, 0, st, h);
                left = idx;
                cur_max = h[idx];
            }
        }
        // index N - 1 -> max last
        int right = N - 1;
        cur_max = h[N - 1];
        for (int idx = N - 2; idx >= 0; idx--) {
            if (h[idx] >= cur_max) {
                dfs(idx, right, 0, st, h);
                right = idx;
                cur_max = h[idx];
            }
        }
        dfs(left, right, 0, st, h);
        std::cout << ans << '\n';
    }
    return 0;
}
