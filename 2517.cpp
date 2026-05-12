#include <iostream>
#include <vector>
#include <algorithm>

template <typename T>
struct segment_tree {
    // ConU's non-recursive uniform segment tree implementation C++
    int n;
    std::vector<T> tree;
    T identity;

    T merge(T a, T b) {
        return a + b;
    }

    segment_tree(const std::vector<T> arr, T id) {
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

void inplace_coordinate_compression(int N, std::vector<int> &A) {
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
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<int> p(N);
    for (auto &i : p) std::cin >> i;
    inplace_coordinate_compression(N, p);
    segment_tree<int> st(std::vector<int>(N, 0), 0);
    for (int v : p) {
        std::cout << 1 + st.query(v + 1, N - 1) << '\n';
        st.update(v, 1);
    }
    return 0;
}
