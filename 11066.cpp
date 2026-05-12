#include <iostream>
#include <vector>

typedef long long ll;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int T;
    std::cin >> T;
    while (T--) {
        int K;
        std::cin >> K;
        std::vector<int> f(K);
        for (auto &i : f) std::cin >> i;
        std::vector<int> psum = {0};
        for (int v : f) psum.push_back(psum.back() + v);
        std::vector<std::vector<ll>> dp(K, std::vector<ll>(K, 1e17));
        for (int start = 0; start + 1 < K; start++) {
            dp[start][start] = 0;
            dp[start][start + 1] = f[start] + f[start + 1];
        }
        dp[K - 1][K - 1] = 0;
        for (int diff = 2; diff < K; diff++) {
            for (int start = 0; start + diff < K; start++) {
                int end = start + diff;
                for (int mid = start; mid < end; mid++) {
                    dp[start][end] = std::min(dp[start][end], dp[start][mid] + dp[mid + 1][end] + psum[end + 1] - psum[start]);
                }
            }
        }
        std::cout << dp[0][K - 1] << '\n';
    }
    return 0;
}
