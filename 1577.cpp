#include <iostream>
#include <map>
#include <utility>
#include <vector>
#include <algorithm>

int main() {
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);

    int N, M, K;
    std::cin >> N >> M >> K;

    std::map<std::pair<int, int>, std::vector<std::pair<int, int> > > blocked;
    while (K--) {
        int x1, y1, x2, y2;
        std::cin >> x1 >> y1 >> x2 >> y2;
        if (x1 + y1 < x2 + y2) {
            std::swap(x1, x2);
            std::swap(y1, y2);
        }
        blocked[std::make_pair(x1, y1)].emplace_back(x2, y2);
    }

    long long dp[N + 1][M + 1];
    dp[0][0] = 1;

    for (int i = 0; i <= N; i++) {
        for (int j = 0; j <= M; j++) {
            if (!i && !j) continue;
            dp[i][j] = 0;
            std::pair<int, int> p = std::make_pair(i, j);
            if (std::find(blocked[p].begin(), blocked[p].end(), std::make_pair(i - 1, j)) == blocked[p].end() && i) dp[i][j] += dp[i - 1][j];
            if (std::find(blocked[p].begin(), blocked[p].end(), std::make_pair(i, j - 1)) == blocked[p].end() && j) dp[i][j] += dp[i][j - 1];
        }
    }

    std::cout << dp[N][M];
    return 0;
}
