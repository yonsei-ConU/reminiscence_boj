#include <iostream>
#include <vector>

inline int abs(int x) {
    return x < 0 ? -x : x;
}

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
        if (l < 0) l = 0;
        if (r >= n) r = n - 1;
        l += n;
        r += n;
        T ret_left = identity;
        T ret_right = identity;
        while (l <= r) {
            if (l & 1) {
                ret_left = merge(ret_left, tree[l]);
                l++;
            }
            if (!(r & 1)) {
                ret_right = merge(tree[r], ret_right);
                r--;
            }
            l >>= 1;
            r >>= 1;
        }
        return merge(ret_left, ret_right);
    }

    T operator[](int idx) {
        return tree[n + idx];
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M, C, D;
    std::cin >> N >> M >> C >> D;
    int interval = D / C;
    std::vector<std::vector<segment_tree<int>>> dp(N + 1, std::vector<segment_tree<int>>(C, segment_tree<int>(std::vector<int>((M + C * 2) / C, 0), 0)));
    for (int i = 1; i <= N; i++) {
        int b;
        std::cin >> b;
        for (int t = 1; t <= M; t++) {
            int q = t / C;
            int r = t % C;
            dp[i][r].update(q, dp[i - 1][r].query(q - interval, q + interval) + M - abs(b - t));
        }
    }
    int ans = 0;
    for (int r = 0; r < C; r++) {
        ans = std::max(ans, dp[N][r].query(0, 1147483647));
    }
    std::cout << ans;
    return 0;
}
