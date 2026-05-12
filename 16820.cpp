#include <iostream>
#include <vector>
#include <queue>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M;
    std::cin >> N >> M;
    std::vector<std::vector<int>> g(N);
    for (int i = 0; i < M; i++) {
        int U, V;
        std::cin >> U >> V;
        g[--U].push_back(--V);
        g[V].push_back(U);
    }
    std::vector<int> dist(N, -1);
    std::queue<int> q;
    q.push(0);
    dist[0] = 0;
    while (!q.empty()) {
        int cur = q.front(); q.pop();
        for (int nxt : g[cur]) {
            if (dist[nxt] == -1) {
                dist[nxt] = dist[cur] + 1;
                q.push(nxt);
            }
        }
    }
    std::vector<std::vector<int>> dp(N, std::vector<int>(2, -1));
    dp[0][0] = 0;
    std::queue<std::vector<int>> q2;
    q2.emplace(2, 0);
    while (!q2.empty()) {
        auto vec = q2.front(); q2.pop();
        int cur = vec[0];
        int parity = vec[1];
        int d = dp[cur][parity];
        for (int nxt : g[cur]) {
            if (dp[nxt][parity ^ 1] == -1) {
                std::vector<int> vv = {nxt, parity ^ 1};
                q2.push(vv);
                dp[nxt][parity ^ 1] = d + 1;
            }
        }
    }
    int odd_ans = 1;
    int even_ans = 2;
    for (int i = 0; i < N; i++) {
        for (int parity = 0; parity < 2; parity++) {
            if (dp[i][parity] == -1) {
                std::cout << -1;
                return 0;
            } else if (parity) {
                odd_ans = std::max(odd_ans, dp[i][parity]);
            } else {
                even_ans = std::max(even_ans, dp[i][parity]);
            }
        }
    }
    std::cout << std::min(odd_ans, even_ans);
    return 0;
}
