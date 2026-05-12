#include <iostream>
#include <vector>
#include <algorithm>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M, C;
    std::cin >> N >> M >> C;
    std::vector<int> m(N);
    int mx = 0;
    for (auto &i : m) {
        std::cin >> i;
        if (i > mx) mx = i;
    }
    std::vector<std::vector<int>> g(N);
    while (M--) {
        int u, v;
        std::cin >> u >> v;
        g[u - 1].push_back(v - 1);
    }
    std::vector<std::vector<int>> dp;
    dp.emplace_back(N, -999999999);
    dp[0][0] = 0;
    for (int t = 1; C * (2 * t + 1) < 2 * mx; t++) {
        std::vector<int> dp_next(N, -999999999);
        for (int i = 0; i < N; i++) {
            for (int nxt : g[i]) {
                dp_next[nxt] = std::max(dp_next[nxt], dp[t - 1][i] + m[nxt]);
            }
        }
        dp.push_back(dp_next);
    }
    std::vector<int> A(dp.size());
    for (int i = 0; i < dp.size(); i++) {
        A[i] = dp[i][0];
    }
    std::vector<int> ans(dp.size(), -999999999);
    ans[0] = 0;
    ans[1] = 0;
    for (int i = 2; i < dp.size(); i++) {
        for (int j = 0; j <= i; j++) {
            ans[i] = std::max(ans[i], ans[i - j] + A[j]);
        }
    }
    int real_ans = 0;
    for (int i = 0; i < dp.size(); i++) {
        real_ans = std::max(real_ans, ans[i] - C * i * i);
    }
    std::cout << real_ans;
    return 0;
}
