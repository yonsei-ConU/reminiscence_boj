#include <iostream>
#include <vector>

typedef long long ll;

void inplace_floyd_warshall(std::vector<std::vector<int>>& g) {
    int n = g.size();
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j) g[i][j] = std::min(g[i][j], g[i][k] + g[k][j]);
            }
        }
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M, K;
    std::cin >> N >> M >> K;
    std::string S;
    std::cin >> S;
    std::vector<int> start;
    for (char s : S) {
        start.push_back(s - 97);
    }
    std::vector<std::vector<int>> cost(M, std::vector<int>(M));
    for (auto &i : cost) {
        for (auto &j : i) std::cin >> j;
    }
    inplace_floyd_warshall(cost);
    std::vector<int> cur_cost(M, 0);
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < K; j++) {
            cur_cost[i] += cost[start[j]][i];
        }
    }
    std::vector<std::vector<ll>> dp(N, std::vector<ll>(M, 1500000000));
    for (int i = 0; i < M; i++) {
        dp[K - 1][i] = cur_cost[i];
    }
    for (int i = K; i < N; i++) {
        ll tmp = 1500000000;
        for (int j = 0; j < M; j++) {
            tmp = std::min(tmp, dp[i - K][j]);
            cur_cost[j] += cost[start[i]][j] - cost[start[i - K]][j];
        }
        for (int j = 0; j < M; j++) {
            dp[i][j] = std::min(tmp + cur_cost[j], dp[i - 1][j] + cost[start[i]][j]);
        }
    }
    std::cout << *std::min_element(dp[N - 1].begin(), dp[N - 1].end());
    return 0;
}
