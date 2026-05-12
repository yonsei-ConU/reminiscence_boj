#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, k;
    std::cin >> n >> k;
    std::vector<std::pair<int, int>> fares(n);
    for (auto &i : fares) std::cin >> i.first >> i.second;
    std::vector<std::vector<int>> passes(k, std::vector<int>(3));
    for (auto &vec : passes) std::cin >> vec[0] >> vec[1] >> vec[2];
    // dp[i]: i-th travel day 까지 비용 최솟값
    std::vector<int> dp(n + 1, 1000000000);
    dp[0] = 0;
    for (int i = 1; i <= n; i++) {
        dp[i] = dp[i - 1] + fares[i - 1].second;
        for (auto &vec : passes) {
            int p = vec[0], d = vec[1], c = vec[2];
            auto it = std::lower_bound(fares.begin(), fares.end(), std::make_pair(fares[i - 1].first - p + 1, 0));
            int idx = it - fares.begin() + 1;
            idx = std::max(idx, i - d + 1);
            dp[i] = std::min(dp[i], dp[idx - 1] + c);
        }
    }
    std::cout << dp[n];
    return 0;
}
