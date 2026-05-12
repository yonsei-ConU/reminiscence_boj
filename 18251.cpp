#include <iostream>
#include <vector>

typedef long long ll;

void inorder(int cur, int d, const std::vector<int> &g, std::vector<std::pair<int, int>> &order, int& D) {
    if (g[cur] == -1) {
        D = d;
        order.emplace_back(cur, d);
        return;
    } else {
        inorder(g[cur], d + 1, g, order, D);
        order.emplace_back(cur, d);
        inorder(g[cur] + 1, d + 1, g, order, D);
    }
}

ll kadane(const std::vector<int> &A) {
    ll ret = -1e18;
    ll cur = 0;
    for (int i : A) {
        cur += i;
        ret = std::max(ret, cur);
        if (cur < 0) cur = 0;
    }
    return ret;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<int> g(N, -1);
    for (int i = 1; i <= N / 2; i++) {
        g[i - 1] = 2 * i - 1;
    }
    std::vector<std::pair<int, int>> order;
    int D = 0;
    inorder(0, 0, g, order, D);
    std::vector<int> W(N);
    for (auto &i : W) std::cin >> i;
    ll ans = -1e18;
    for (int d = D; d >= 0; d--) {
        std::vector<std::pair<int, int>> new_order;
        for (auto &p : order) {
            if (p.second <= d) {
                new_order.emplace_back(p);
            }
        }
        std::swap(order, new_order);
        for (int d2 = d; d2 >= 0; d2--) {
            std::vector<int> candidates;
            for (auto &p : order) {
                if (p.second >= d2) {
                    candidates.push_back(W[p.first]);
                }
            }
            ans = std::max(ans, kadane(candidates));
        }
    }
    std::cout << ans;
    return 0;
}
