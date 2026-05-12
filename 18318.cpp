#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

typedef long long ll;
const ll MX = 1000000000000000000;

std::vector<int> coordinate_compression(int N, std::vector<int> A) {
    std::vector<int> id(N);
    for (int i = 0; i < N; i++) {
        id[i] = i;
    }
    std::sort(id.begin(), id.end(), [&](int a, int b) {
        return A[a] < A[b];
    });

    int newX = 0;
    for (int i = 1; i < N; i++) {
        if (A[id[i - 1]] < A[id[i]]) {
            A[id[i - 1]] = newX++;
        } else {
            A[id[i - 1]] = newX;
        }
    }
    A[id[N - 1]] = newX;
    return A;
}

template <typename T>
struct segment_tree {
    // ConU's non-recursive uniform segment tree implementation C++
    int n;
    std::vector<T> tree;
    T identity;

    T merge(T a, T b) {
        return std::min(a, b);
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
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, P;
    std::cin >> N >> P;
    std::vector<int> x, y;
    for (int i = 0; i < P; i++) {
        int x1, x2, y1, y2;
        std::cin >> x1 >> y1 >> x2 >> y2;
        x.push_back(x1);
        x.push_back(x2);
        y.push_back(y1);
        y.push_back(y2);
    }
    auto cx = coordinate_compression(P * 2, x);
    auto cy = coordinate_compression(P * 2, y);
    std::sort(x.begin(), x.end());
    std::sort(y.begin(), y.end());
    std::vector<int> distinct_x, distinct_y;
    for (int v : x) {
        if (distinct_x.empty() || distinct_x.back() < v) distinct_x.push_back(v);
    }
    for (int v : y) {
        if (distinct_y.empty() || distinct_y.back() < v) distinct_y.push_back(v);
    }
    segment_tree<ll> st(std::vector<ll>(distinct_y.size(), MX), MX);
    st.update(0, 0);
    std::vector<std::vector<int>> springboards(P);
    for (int i = 0; i < P; i++) {
        springboards[i] = {cx[2 * i], cy[2 * i], cx[2 * i + 1], cy[2 * i + 1]};
    }
    std::sort(springboards.begin(), springboards.end());
    std::priority_queue<std::pair<int, std::pair<int, ll>>> to_update;
    for (auto &vec : springboards) {
        while (!to_update.empty() && -to_update.top().first <= vec[0]) {
            auto [idx, val] = to_update.top().second; to_update.pop();
            if (val < st.tree[st.n + idx]) st.update(idx, val);
        }
        ll cur = st.query(0, vec[1]);
        to_update.push({-vec[2], {vec[3], cur + distinct_x[vec[0]] + distinct_y[vec[1]] - distinct_x[vec[2]] - distinct_y[vec[3]]}});
    }
    while (!to_update.empty()) {
        auto [idx, val] = to_update.top().second; to_update.pop();
        if (val < st.tree[st.n + idx]) st.update(idx, val);
    }
    std::cout << st.query(0, (int)distinct_y.size() - 1) + 2 * N;
    return 0;
}
